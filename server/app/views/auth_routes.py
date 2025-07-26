from flask import Blueprint
from app.controllers import auth_controller
from app.middlewares import auth_middleware

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    return auth_controller.register_user()

@bp.route('/login', methods=['POST'])
def login():
    return auth_controller.login_user()

@bp.route('/protected', methods=['GET'])
@auth_middleware.validate_token
def protected():
    return auth_controller.protected_route()
