from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=None):
    app = Flask(__name__)

    if testing is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DEV_DATABASE_URI')
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('TEST_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.planet import Planet

    from .routes import planets_bp

    app.register_blueprint(planets_bp)
    
    return app
