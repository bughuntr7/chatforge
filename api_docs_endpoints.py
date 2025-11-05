"""
API Documentation decorators for endpoints
This file provides easy-to-use decorators for documenting endpoints
"""
from flask_restx import Namespace
from functools import wraps

def document_endpoint(namespace, description, params=None, responses=None):
    """
    Decorator to document an endpoint with Swagger
    
    Usage:
        @document_endpoint(
            auth_ns,
            'User login endpoint',
            params={'email': 'string', 'password': 'string'},
            responses={200: 'Success', 401: 'Unauthorized'}
        )
        def login():
            ...
    """
    def decorator(func):
        @namespace.doc(description=description)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

