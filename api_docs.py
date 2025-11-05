from flask_restx import Api, Resource, fields
from flask import Blueprint

api_blueprint = Blueprint('api', __name__)
api = Api(
    api_blueprint,
    version='1.0.0',
    title='ChatForge API',
    description='Scalable AI Chatbot API built with Flask, OpenAI, and vector memory',
    doc='/docs/',
    prefix='/api',
    authorizations={
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Type in the *\'Value\'* input box: **Bearer {token}**'
        }
    },
    security='Bearer'
)

# Namespace definitions
auth_ns = api.namespace('auth', description='Authentication endpoints')
bot_ns = api.namespace('bot', description='Chatbot management endpoints')
knowledge_ns = api.namespace('knowledge', description='Knowledge base management')
chat_ns = api.namespace('chat', description='Chat and conversation endpoints')
ticket_ns = api.namespace('tickets', description='Support ticket endpoints')
payment_ns = api.namespace('payment', description='Payment processing endpoints')
shopify_ns = api.namespace('shopify', description='Shopify integration endpoints')
wordpress_ns = api.namespace('wordpress', description='WordPress integration endpoints')

# Request/Response models
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

register_model = api.model('Register', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'language': fields.String(required=True, description='Language preference'),
    'com_name': fields.String(required=True, description='Company name'),
    'com_vat': fields.String(required=True, description='Company VAT'),
    'com_street': fields.String(required=True, description='Company street'),
    'com_street_number': fields.String(required=True, description='Street number'),
    'com_city': fields.String(required=True, description='City'),
    'com_postal': fields.String(required=True, description='Postal code'),
    'com_country': fields.String(required=True, description='Country'),
    'com_website': fields.String(required=True, description='Company website')
})

chat_query_model = api.model('ChatQuery', {
    'input': fields.String(required=True, description='User message'),
    'botId': fields.Integer(required=True, description='Bot ID'),
    'userId': fields.Integer(required=True, description='User ID'),
    'sessionId': fields.String(required=True, description='Session ID'),
    'createdAt': fields.String(required=True, description='Creation timestamp'),
    'website': fields.String(required=True, description='Website URL')
})

create_bot_model = api.model('CreateBot', {
    'name': fields.String(required=True, description='Bot name'),
    'user_id': fields.Integer(required=True, description='User ID'),
    'color': fields.String(required=True, description='Bot color'),
    'active': fields.String(required=True, description='Active status'),
    'start_time': fields.String(required=True, description='Start time'),
    'end_time': fields.String(required=True, description='End time'),
    'knowledge_base': fields.String(required=True, description='Knowledge base ID')
})

error_response_model = api.model('Error', {
    'error': fields.String(description='Error message'),
    'status': fields.Integer(description='HTTP status code'),
    'code': fields.String(description='Error code')
})

success_response_model = api.model('Success', {
    'message': fields.String(description='Success message'),
    'status': fields.Integer(description='HTTP status code'),
    'data': fields.Raw(description='Response data')
})

# Documentation endpoints
@api_blueprint.route('/')
class APIInfo(Resource):
    @api.doc('api_info')
    @api.marshal_with(success_response_model)
    def get(self):
        """API information and health check"""
        return {
            'message': 'ChatForge API is running',
            'status': 200,
            'data': {
                'version': '1.0.0',
                'docs': '/api/docs/'
            }
        }

# Auth namespace endpoints
@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.doc('login')
    @auth_ns.expect(login_model)
    @auth_ns.marshal_with(success_response_model, code=200)
    @auth_ns.marshal_with(error_response_model, code=401)
    def post(self):
        """
        User login endpoint
        
        Returns JWT access token on successful authentication
        """
        pass

@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.doc('register')
    @auth_ns.expect(register_model)
    @auth_ns.marshal_with(success_response_model, code=201)
    @auth_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        User registration endpoint
        
        Creates a new user account
        """
        pass

# Bot namespace endpoints
@bot_ns.route('/query')
class ChatQuery(Resource):
    @bot_ns.doc('chat_query')
    @bot_ns.expect(chat_query_model)
    @bot_ns.marshal_with(success_response_model, code=200)
    @bot_ns.marshal_with(error_response_model, code=403)
    def post(self):
        """
        Send a chat query to the bot
        
        Processes user message and returns AI-generated response
        """
        pass

@bot_ns.route('/create_bot')
class CreateBot(Resource):
    @bot_ns.doc('create_bot', security='Bearer')
    @bot_ns.expect(create_bot_model)
    @bot_ns.marshal_with(success_response_model, code=201)
    @bot_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        Create a new chatbot
        
        Requires JWT authentication
        """
        pass

