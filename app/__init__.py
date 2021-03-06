from flask import Flask
from .config import Config
from .models import db

from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(auth)
    return app