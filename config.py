import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize the extensions globally but do not bind them to the app yet
db = SQLAlchemy()
bcrypt = Bcrypt()

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT secret key
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_secret_key')  # Change this

    # Pesapal API configuration
    PESAPAL_API_URL = os.getenv('PESAPAL_API_URL', 'https://www.pesapal.com/API/PostPayment')  # Pesapal API URL
    PESAPAL_API_KEY = os.getenv('PESAPAL_API_KEY', 'your_pesapal_api_key')  # Pesapal API Key
    PESAPAL_SECRET_KEY = os.getenv('PESAPAL_SECRET_KEY', 'your_pesapal_secret_key')  # Pesapal Secret Key
