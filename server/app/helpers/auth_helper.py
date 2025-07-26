import jwt
from datetime import datetime, timedelta
from flask import current_app

def generate_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token
