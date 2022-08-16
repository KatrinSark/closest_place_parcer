from flask import Flask
import os

from main.extensions import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:docker@db/postgres"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Initialize app with database
    db.init_app(app)

    from main.flask_api import api
    app.register_blueprint(api)

    return app


app = create_app()




