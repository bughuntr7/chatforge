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

@bot_ns.route('/get_chatbots')
class GetChatbots(Resource):
    @bot_ns.doc('get_chatbots', security='Bearer')
    @bot_ns.param('userId', 'User ID', required=True)
    @bot_ns.marshal_with(success_response_model, code=200)
    @bot_ns.marshal_with(error_response_model, code=400)
    def get(self):
        """
        Get all chatbots for a user
        
        Requires JWT authentication
        """
        pass

@bot_ns.route('/get_chatbot_data')
class GetChatbotData(Resource):
    @bot_ns.doc('get_chatbot_data', security='Bearer')
    @bot_ns.param('botId', 'Bot ID', required=True)
    @bot_ns.param('userId', 'User ID', required=True)
    @bot_ns.marshal_with(success_response_model, code=200)
    @bot_ns.marshal_with(error_response_model, code=400)
    def get(self):
        """
        Get detailed data for a specific chatbot
        
        Requires JWT authentication
        """
        pass

@bot_ns.route('/del_bot')
class DeleteBot(Resource):
    @bot_ns.doc('del_bot', security='Bearer')
    @bot_ns.expect(api.model('DeleteBot', {
        'botId': fields.Integer(required=True, description='Bot ID to delete')
    }))
    @bot_ns.marshal_with(success_response_model, code=200)
    @bot_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        Delete a chatbot
        
        Requires JWT authentication
        """
        pass

@bot_ns.route('/update_chatbot')
class UpdateChatbot(Resource):
    @bot_ns.doc('update_chatbot', security='Bearer')
    @bot_ns.expect(create_bot_model)
    @bot_ns.marshal_with(success_response_model, code=200)
    @bot_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        Update chatbot settings
        
        Requires JWT authentication
        """
        pass

@bot_ns.route('/del_messages')
class DeleteMessages(Resource):
    @bot_ns.doc('del_messages', security='Bearer')
    @bot_ns.expect(api.model('DeleteMessages', {
        'sessionId': fields.String(required=True, description='Session ID')
    }))
    @bot_ns.marshal_with(success_response_model, code=200)
    def post(self):
        """
        Delete conversation messages for a session
        
        Requires JWT authentication
        """
        pass

# Auth namespace endpoints - additional
@auth_ns.route('/get_user')
class GetUser(Resource):
    @auth_ns.doc('get_user', security='Bearer')
    @auth_ns.expect(api.model('GetUser', {
        'userID': fields.Integer(required=True, description='User ID')
    }))
    @auth_ns.marshal_with(success_response_model, code=200)
    @auth_ns.marshal_with(error_response_model, code=404)
    def post(self):
        """
        Get user information
        
        Requires JWT authentication
        """
        pass

@auth_ns.route('/update_user')
class UpdateUser(Resource):
    @auth_ns.doc('update_user', security='Bearer')
    @auth_ns.expect(register_model)
    @auth_ns.marshal_with(success_response_model, code=200)
    @auth_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        Update user information
        
        Requires JWT authentication
        """
        pass

@auth_ns.route('/forgot_password')
class ForgotPassword(Resource):
    @auth_ns.doc('forgot_password')
    @auth_ns.expect(api.model('ForgotPassword', {
        'email': fields.String(required=True, description='User email')
    }))
    @auth_ns.marshal_with(success_response_model, code=200)
    @auth_ns.marshal_with(error_response_model, code=404)
    def post(self):
        """
        Request password reset
        
        Sends password reset email to user
        """
        pass

@auth_ns.route('/reset_with_token')
class ResetPassword(Resource):
    @auth_ns.doc('reset_password')
    @auth_ns.expect(api.model('ResetPassword', {
        'token': fields.String(required=True, description='Reset token'),
        'password': fields.String(required=True, description='New password')
    }))
    @auth_ns.marshal_with(success_response_model, code=201)
    @auth_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        Reset password with token
        
        Resets user password using verification token
        """
        pass

# Knowledge namespace endpoints
upload_document_model = api.model('UploadDocument', {
    'name': fields.String(required=True, description='Knowledge base name'),
    'userID': fields.Integer(required=True, description='User ID'),
    'files': fields.List(fields.Raw, description='Document files'),
    'qa': fields.String(description='Q&A JSON'),
    'docs': fields.String(description='Docs JSON'),
    'urls': fields.String(description='URLs JSON')
})

@knowledge_ns.route('/upload_document')
class UploadDocument(Resource):
    @knowledge_ns.doc('upload_document', security='Bearer')
    @knowledge_ns.expect(upload_document_model)
    @knowledge_ns.marshal_with(success_response_model, code=201)
    @knowledge_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        Upload documents to knowledge base
        
        Supports multiple file types (PDF, DOCX, TXT, etc.)
        Requires JWT authentication
        """
        pass

@knowledge_ns.route('/get_knowledge_bases')
class GetKnowledgeBases(Resource):
    @knowledge_ns.doc('get_knowledge_bases', security='Bearer')
    @knowledge_ns.param('userId', 'User ID', required=True)
    @knowledge_ns.marshal_with(success_response_model, code=200)
    @knowledge_ns.marshal_with(error_response_model, code=400)
    def get(self):
        """
        Get all knowledge bases for a user
        
        Requires JWT authentication
        """
        pass

@knowledge_ns.route('/get_knowledge_base')
class GetKnowledgeBase(Resource):
    @knowledge_ns.doc('get_knowledge_base', security='Bearer')
    @knowledge_ns.param('baseId', 'Knowledge base ID', required=True)
    @knowledge_ns.marshal_with(success_response_model, code=200)
    @knowledge_ns.marshal_with(error_response_model, code=404)
    def get(self):
        """
        Get detailed knowledge base information
        
        Includes documents, websites, and texts
        Requires JWT authentication
        """
        pass

@knowledge_ns.route('/del_knowledgebase')
class DeleteKnowledgeBase(Resource):
    @knowledge_ns.doc('del_knowledgebase', security='Bearer')
    @knowledge_ns.expect(api.model('DeleteKB', {
        'baseId': fields.Integer(required=True, description='Knowledge base ID')
    }))
    @knowledge_ns.marshal_with(success_response_model, code=200)
    def post(self):
        """
        Delete a knowledge base
        
        Requires JWT authentication
        """
        pass

# Ticket namespace endpoints
book_ticket_model = api.model('BookTicket', {
    'botId': fields.Integer(required=True, description='Bot ID'),
    'userIndex': fields.String(required=True, description='User index'),
    'sessionId': fields.String(required=True, description='Session ID'),
    'email': fields.String(required=True, description='Email address'),
    'content': fields.String(required=True, description='Ticket content'),
    'website': fields.String(required=True, description='Website URL'),
    'createdAt': fields.String(required=True, description='Creation timestamp')
})

@ticket_ns.route('/book')
class BookTicket(Resource):
    @ticket_ns.doc('book_ticket')
    @ticket_ns.expect(book_ticket_model)
    @ticket_ns.marshal_with(success_response_model, code=201)
    @ticket_ns.marshal_with(error_response_model, code=500)
    def post(self):
        """
        Create a support ticket
        
        Books a ticket and sends email notification
        """
        pass

@ticket_ns.route('/get_tickets')
class GetTickets(Resource):
    @ticket_ns.doc('get_tickets', security='Bearer')
    @ticket_ns.expect(api.model('GetTickets', {
        'userID': fields.Integer(required=True, description='User ID')
    }))
    @ticket_ns.marshal_with(success_response_model, code=200)
    def post(self):
        """
        Get all tickets for a user
        
        Requires JWT authentication
        """
        pass

# Chat log namespace endpoints
@chat_ns.route('/get_chat')
class GetChat(Resource):
    @chat_ns.doc('get_chat', security='Bearer')
    @chat_ns.expect(api.model('GetChat', {
        'userID': fields.Integer(required=True, description='User ID')
    }))
    @chat_ns.marshal_with(success_response_model, code=200)
    def post(self):
        """
        Get chat logs for a user
        
        Requires JWT authentication
        """
        pass

@chat_ns.route('/get_log_data')
class GetLogData(Resource):
    @chat_ns.doc('get_log_data', security='Bearer')
    @chat_ns.expect(api.model('GetLogData', {
        'sessionId': fields.String(required=True, description='Session ID')
    }))
    @chat_ns.marshal_with(success_response_model, code=200)
    def post(self):
        """
        Get detailed conversation log for a session
        
        Requires JWT authentication
        """
        pass

# Payment namespace endpoints
checkout_session_model = api.model('CheckoutSession', {
    'price_id': fields.String(required=True, description='Stripe price ID'),
    'email': fields.String(required=True, description='Customer email')
})

@payment_ns.route('/create-checkout-session')
class CreateCheckoutSession(Resource):
    @payment_ns.doc('create_checkout')
    @payment_ns.expect(checkout_session_model)
    @payment_ns.marshal_with(success_response_model, code=200)
    @payment_ns.marshal_with(error_response_model, code=400)
    def post(self):
        """
        Create Stripe checkout session
        
        Returns Stripe checkout session URL
        """
        pass

@payment_ns.route('/webhook')
class PaymentWebhook(Resource):
    @payment_ns.doc('payment_webhook')
    def post(self):
        """
        Stripe webhook endpoint
        
        Handles Stripe payment events
        """
        pass

# Shopify namespace endpoints
@shopify_ns.route('/shopifyinstall')
class ShopifyInstall(Resource):
    @shopify_ns.doc('shopify_install')
    @shopify_ns.param('shop', 'Shop domain', required=True)
    @shopify_ns.param('hmac', 'HMAC signature', required=True)
    @shopify_ns.param('timestamp', 'Timestamp', required=True)
    def get(self):
        """
        Shopify app installation endpoint
        
        Initiates OAuth flow for Shopify app
        """
        pass

@shopify_ns.route('/active_chatbots')
class ActiveChatbots(Resource):
    @shopify_ns.doc('active_chatbots')
    @shopify_ns.param('shop', 'Shop domain', required=True)
    @shopify_ns.marshal_with(success_response_model, code=200)
    def get(self):
        """
        Get active chatbots for a Shopify store
        """
        pass

# WordPress namespace endpoints
@wordpress_ns.route('/wordpressinstall')
class WordPressInstall(Resource):
    @wordpress_ns.doc('wordpress_install')
    @wordpress_ns.param('website_url', 'WordPress website URL', required=True)
    @wordpress_ns.param('access_token', 'Access token', required=True)
    def get(self):
        """
        WordPress plugin installation endpoint
        
        Initiates connection with WordPress site
        """
        pass

