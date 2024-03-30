from flask import Blueprint
from bad_code.bad_blog.db.db import get_db

blueprint = Blueprint('bad_blog', __name__)

from .routes.routes import *

__all__ = ['blueprint']