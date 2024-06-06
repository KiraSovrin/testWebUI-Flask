# app/main/__init__.py

from flask import Blueprint
bp = Blueprint('main', __name__)
# Import routes after the blueprint is defined to avoid circular import
from app.main import routes