import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow
from flask_paranoid import Paranoid
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv


APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
app = Flask(__name__)
paranoid = Paranoid(app)
paranoid.redirect_view = '/'
app.config.from_object('config')

Bootstrap(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_message = "You must be logged in to access this page"
login_manager.login_view = "auth.login"

from .models import user

from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)
