from flask import Flask, send_from_directory, request, redirect, url_for, render_template
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.utils import secure_filename
from . import app
from .models import users
import os

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