from flask import Flask
from utils.config import get
app = Flask(__name__)
app.debug = get("FLASK_DEBUG", int) or False
app.secret_key = 'SECRET_KEY'

from .users import users_blueprint
from .views import main, resume, contact
app.register_blueprint(users_blueprint)