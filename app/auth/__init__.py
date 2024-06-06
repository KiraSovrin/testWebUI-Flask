# app/auth/__init__.py

from flask import Blueprint
bp = Blueprint('auth', __name__)
# Import routes after the blueprint is defined to avoid circular import
from app.auth import routes
