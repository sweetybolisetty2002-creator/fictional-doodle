from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from urllib.parse import urlparse
from .models import db, User, Post
from azure.storage.blob import BlobServiceClient

views = Blueprint('views', __name__)

def get_blob_service():
    account_url = f"https://{current_app.config['BLOB_ACCOUNT']}.blob.core.windows.net"
    credential = current_app.config['BLOB_STORAGE_KEY']
    return BlobServiceClient(account_url=account_url, credential=credential)

@views.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@views.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    # Your create logic
    pass

# ...other routes
