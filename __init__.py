from flask import Flask
from flask_session import Session

app = Flask(__name__)
app.config.from_object('config.Config')

# Setup session management
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

from . import views  # Import routes from views.py
