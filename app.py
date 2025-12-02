from flask import Flask
from src.extensions import db
from src.routes.user_routes import user_bp
from config import Config
from src.celery_utils.tasks import print_hello

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Register Routers
    app.register_blueprint(user_bp, url_prefix="/users")

    return app
