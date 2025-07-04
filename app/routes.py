# app/routes.py
from flask import Blueprint

bp = Blueprint('main', __name__)  # ← No more "from app import create_app"

@bp.route('/')
def home():
    return "Hello World"