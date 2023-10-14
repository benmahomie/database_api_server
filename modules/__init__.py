from flask import Flask
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, ALL
import logging
import secrets

# Signature configuration
# secret = 'secret' # Uncomment for testing (not secure)
secret = secrets.token_hex(16) # Uncomment for deployment (uses HMAC hash like SHA-256)

# Start Flask App
app = Flask(__name__)
app.secret_key = secret 

# Login Settings
login_manager = LoginManager()
login_manager.init_app(app)

# Database Configuration (points to the folder holding database)
files = UploadSet('files', ALL)
app.config['UPLOADED_FILES_DEST'] = 'file_storage' 
configure_uploads(app, files)

# Logging Configuration (for hard-to-catch issues)
logging.basicConfig(level=logging.DEBUG) 

# App Routes
from . import routes