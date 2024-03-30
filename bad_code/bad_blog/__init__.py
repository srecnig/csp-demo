from flask import Blueprint
from bad_code.db import get_db

blueprint = Blueprint('bad_blog', __name__)

from .routes import *

__all__ = ['blueprint']