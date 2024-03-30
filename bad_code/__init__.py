import os

from flask import Flask

from bad_code.db import init_app
from bad_code.bad_blog import blueprint as blog_blueprint


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'bad_code.sqlite'),
    )
    init_app(app)
    app.register_blueprint(blog_blueprint)
    app.add_url_rule('/', endpoint='index')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app