from flask import Flask, send_from_directory, request, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_uploads import UploadSet, configure_uploads, ALL
from werkzeug.utils import secure_filename
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'secret'

login_manager = LoginManager()
login_manager.init_app(app)

# Configure Flask-Uploads
files = UploadSet('files', ALL)
app.config['UPLOADED_FILES_DEST'] = 'file_storage'
configure_uploads(app, files)

# User data
class User(UserMixin):
    def __init__(self, id, permission='read', password=None):
        self.id = id
        self.password = password
        self.permission = permission

users = {
    'admin': User('admin', permission='edit', password='admin'),
    'user': User('user', permission='download' password='user'),
    'guest': User('guest', permission='read', password='guest')
    }

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Routes
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('upload'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if current_user.permission != 'edit':
        return "Permission Denied"
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            secure_name = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join('file_storage', secure_name))
            return f"File {secure_name} uploaded."
    return render_template('upload.html')

@app.route('/files')
@login_required
def files():
    files = os.listdir('file_storage')
    return render_template('files.html', files=files, permission=current_user.permission)

@app.route('/files/<path:filename>', methods=['GET'])
@login_required
def download_file(filename):
    if current_user.permission in ['download', 'edit']:
        return send_from_directory(directory='file_storage', filename=filename)
    else:
        return "Permission Denied"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)