from flask import jsonify

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

