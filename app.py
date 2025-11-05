import os
import uuid
import time
import pymysql
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from flask import Flask, request, jsonify, make_response
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from api.auth import user_blueprint
from api.bot import bot_blueprint
from api.knowledge import knowledge_blueprint
from api.chatlog import log_blueprint
from api.tickets import ticket_blueprint
from api.payment import payment_blueprint
from api.shopify import shopify_blueprint, sync_products
from api.mautic import delete_mautic_contact
from api.wordpress import wordpress_blueprint
from api_docs import api_blueprint
from models import db, User
from datetime import timedelta
from utils.common import get_bucket_name
import cProfile
import pstats

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SHOPIFY_DB_URI")
# app.config['SQLALCHEMY_BINDS'] = {
#    'shopify': os.getenv('SHOPIFY_DB_URI')
# }
# from sqlalchemy import create_engine

# engine = create_engine(os.getenv('DB_URI'), connect_args={'ssl': {'sslmode': 'REQUIRED'}})

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db?check_same_thread=False&mode=WAL'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.googlemail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['SCHEDULER_API_ENABLED'] = True

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=3)

# app.config['JWT_TOKEN_LOCATION'] = ['cookies']
# app.config['JWT_COOKIE_SECURE'] = True  # Set to False if not using https
# app.config['JWT_COOKIE_CSRF_PROTECT'] = True  # CSRF protection
# Initialize JWTManager
jwt = JWTManager(app)

db.init_app(app)
migrate = Migrate(app, db)

# Configure logging
if not app.debug:
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    app.logger.setLevel(getattr(logging, log_level, logging.INFO))
    
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = RotatingFileHandler('logs/chatforge.log', maxBytes=10240000, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('ChatForge startup')

def scheduled_task():
   with app.app_context():
      sync_products()

scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_task, trigger="interval", minutes=60)
scheduler.start()
# CORS(app, supports_credentials=True, origins=['https://your-frontend-domain.com'])
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

app.register_blueprint(api_blueprint)
app.register_blueprint(user_blueprint, url_prefix='/api')
app.register_blueprint(bot_blueprint, url_prefix='/api')
app.register_blueprint(knowledge_blueprint, url_prefix='/api')
app.register_blueprint(log_blueprint, url_prefix='/api')
app.register_blueprint(ticket_blueprint, url_prefix='/api')
app.register_blueprint(shopify_blueprint, url_prefix='/api')
app.register_blueprint(payment_blueprint)
app.register_blueprint(wordpress_blueprint, url_prefix='/api')

get_bucket_name()

@app.route("/")
def index():
    """Health check endpoint for the ChatForge API."""
    return jsonify({
        "message": "ChatForge API is running",
        "status": "healthy",
        "version": "1.0.0"
    }), 200

if __name__ == '__main__':
   # Start profiling
   profiler = cProfile.Profile()
   profiler.enable()

   app.run(debug=True)

   # Stop profiling and save the results
   profiler.disable()
   stats = pstats.Stats(profiler).sort_stats('cumulative')
   stats.print_stats()
