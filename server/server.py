from flask import Flask
from app.config import Config
from app.extensions import db, migrate, bcrypt, cors
from app.views import auth_routes
from app.models import user

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    cors.init_app(app) # Initialize CORS

    app.register_blueprint(auth_routes.bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
