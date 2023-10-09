from flask import Flask
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, ALL
import logging

app = Flask(__name__)
app.secret_key = 'secret'

login_manager = LoginManager()
login_manager.init_app(app)

files = UploadSet('files', ALL)
app.config['UPLOADED_FILES_DEST'] = 'file_storage'
configure_uploads(app, files)

logging.basicConfig(level=logging.DEBUG)

from . import routes