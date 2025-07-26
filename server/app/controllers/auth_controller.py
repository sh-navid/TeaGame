from flask import jsonify, request
from app.models.user import User
from app.extensions import db
from app.helpers import auth_helper

def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400
    
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return jsonify({'message': 'Email already exists'}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing credentials'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = auth_helper.generate_token(user)
    return jsonify({'token': token}), 200

def protected_route():
    user = request.user
    return jsonify({'message': 'This is a protected route', 'user': user.username}), 200
