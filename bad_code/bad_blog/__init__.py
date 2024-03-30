from flask import Blueprint

blueprint = Blueprint("bad_blog", __name__)

from .routes.routes import *  # noqa

__all__ = ["blueprint"]
