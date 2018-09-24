from flask import Flask, url_for
from jinja2 import Environment

import os


def create_app(test_config=None):
    app = Flask(__name__, 
                instance_relative_config=True,
                template_folder='templates',
                static_url_path='/assets')
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql://root:jkiwen_18@localhost:3306/world'
    )

    print(app.url_map)

    # 注册URL规则
    app.add_url_rule('/docStatic', endpoint='docStatic')

    print(app.url_map)

    with app.test_request_context():
        print(url_for('docStatic'))

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # from backend import db
    # db.init_app(app)

    from . import views

    views.ListView.register(app)

    return app
