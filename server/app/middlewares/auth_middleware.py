from flask import request, jsonify
import jwt
from app.models.user import User
from flask import current_app
from functools import wraps


def validate_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = data['user_id']
            user = User.query.get(user_id)
            if user is None:
                return jsonify({'message': 'Invalid token - user not found'}), 401
            request.user = user
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        except Exception as e:
            return jsonify({'message': 'Internal server error'}), 500

        return f(*args, **kwargs)

    return decorated_function
