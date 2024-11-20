from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp
from routes.payment_routes import payment_bp  # Import the new payment routes
from models import db

# Initialize extensions
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Config from config.py

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(payment_bp, url_prefix='/payment')  # Register the payment blueprint

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
