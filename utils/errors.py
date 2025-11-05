from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from werkzeug.exceptions import BadRequest

def error_response(message, status_code=500, error_code=None, details=None):
    """
    Create a standardized error response.
    
    Args:
        message: Human-readable error message
        status_code: HTTP status code (default: 500)
        error_code: Machine-readable error code (optional)
        details: Additional error details (optional)
    
    Returns:
        Tuple of (jsonify response, status_code)
    """
    response = {
        'error': message,
        'status': status_code
    }
    
    if error_code:
        response['code'] = error_code
    
    if details:
        response['details'] = details
    
    return jsonify(response), status_code

def success_response(data=None, message=None, status_code=200):
    """
    Create a standardized success response.
    
    Args:
        data: Response data (optional)
        message: Success message (optional)
        status_code: HTTP status code (default: 200)
    
    Returns:
        Tuple of (jsonify response, status_code)
    """
    response = {'status': status_code}
    
    if message:
        response['message'] = message
    
    if data:
        response['data'] = data
    
    return jsonify(response), status_code

def handle_exception(e):
    """
    Handle exceptions and return appropriate error response.
    
    Args:
        e: Exception object
    
    Returns:
        Tuple of (jsonify response, status_code)
    """
    if isinstance(e, ValueError):
        return error_response('Invalid input value', 400, 'VALIDATION_ERROR', str(e))
    elif isinstance(e, KeyError):
        return error_response(f'Missing required field: {str(e)}', 400, 'VALIDATION_ERROR')
    elif isinstance(e, IntegrityError):
        return error_response('Database integrity error', 409, 'CONFLICT_ERROR', str(e))
    elif isinstance(e, SQLAlchemyError):
        return error_response('Database error', 500, 'DATABASE_ERROR', str(e))
    elif isinstance(e, BadRequest):
        return error_response('Bad request', 400, 'BAD_REQUEST', str(e))
    else:
        return error_response('Internal server error', 500, 'INTERNAL_ERROR', str(e))

