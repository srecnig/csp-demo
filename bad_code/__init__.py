import os

from flask import Flask

from bad_code.bad_blog import blueprint as blog_blueprint
from bad_code.bad_blog.db import close_db, init_database


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "bad_code.sqlite"),
    )

    # database handling
    app.teardown_appcontext(close_db)

    # add blog endpoints
    app.register_blueprint(blog_blueprint)
    app.add_url_rule("/", endpoint="index")

    # register cli commands
    app.cli.add_command(init_database)

    return app
