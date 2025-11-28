import os

from flask import Flask
from src.extensions import db
from src.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # pg_user = os.getenv("POSTGRES_USER")
    # pg_password = os.getenv("POSTGRES_PASSWORD")
    # pg_host = os.getenv("POSTGRES_HOST")
    # pg_port = os.getenv("POSTGRES_PORT")
    # pg_db = os.getenv("POSTGRES_DB")
    #
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register Routers
    app.register_blueprint(user_bp, url_prefix="/users")

    return app
