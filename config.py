import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-insecure-key-for-dev')
    SESSION_COOKIE_SECURE = True

    # Database (example for SQLite - adjust for PostgreSQL/MySQL)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask settings
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    FLASK_DEBUG = False

class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    SESSION_COOKIE_SECURE = False  # Allow HTTP in dev

class ProductionConfig(Config):
    SECRET_KEY = 'your-production-key'
    FLASK_ENV = 'production'