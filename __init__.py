from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .models import db, User
from .views import views

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'GvnN4QwQN1wKOaa0RlNDS_G3DDvMvXh9tgmevZ24G5A='
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-db-file.db'
    app.config['BLOB_ACCOUNT'] = 'images11'
    app.config['BLOB_STORAGE_KEY'] = ''
    app.config['BLOB_CONTAINER'] = 'images'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(views)
    return app

