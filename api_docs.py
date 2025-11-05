from flask_restx import Api, Resource, fields
from flask import Blueprint

api_blueprint = Blueprint('api', __name__)
api = Api(
    api_blueprint,
    version='1.0.0',
    title='ChatForge API',
    description='Scalable AI Chatbot API built with Flask, OpenAI, and vector memory',
    doc='/docs/',
    prefix='/api'
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
    def get(self):
        """API information and health check"""
        return {
            'message': 'ChatForge API is running',
            'status': 'healthy',
            'version': '1.0.0',
            'docs': '/api/docs/'
        }

