from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity,decode_token
from models.user import User

def jwt_middleware(fn):
   def wrapper(*args, **kwargs):
       try:
           # Extract the access token from the "Authorization" header
           auth_header = request.headers.get('Authorization')
           if not auth_header or not auth_header.startswith('Bearer '):
               return jsonify(message='Access token is missing'), 401

           access_token = auth_header.split(' ')[1]
           decoded_token = decode_token(access_token)

           if 'sub' not in decoded_token:
              return jsonify(message='Invalid access token'), 401
           
           verify_jwt_in_request(optional=True)
           current_user = get_jwt_identity()

           print("Additional Claims:", decoded_token.get('user_id'))
           user = User.query.get(current_user)
           if not user:
            return jsonify(message='User not found'), 401

           return fn(current_user, *args, **kwargs)  # Pass the current user to the wrapped route
       except Exception as e:
           return jsonify(message='Token validation failed', error=str(e)), 401
   return wrapper