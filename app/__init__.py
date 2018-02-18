import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])

    db.init_app(app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from .blueprints.index import app as index
    app.register_blueprint(index)

