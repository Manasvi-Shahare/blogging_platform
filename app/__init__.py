from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
auth = HTTPBasicAuth()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from .routes import bp as routes_bp
    from .auth import auth_routes as auth_bp
    app.register_blueprint(routes_bp)
    app.register_blueprint(auth_bp)

    return app
