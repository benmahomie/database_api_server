from flask_login import UserMixin
from . import login_manager

# User Object Class for Flask-Login
class User(UserMixin):
    def __init__(self, id, permission='read', password=None):
        self.id = id
        self.password = password
        self.permission = permission

# User Configuration (ID, Permission Level, Password)
users = {
    'admin': User(id='admin', permission='edit', password='admin'),
    'user': User(id='user', permission='download', password='user'),
    'guest': User(id='guest', permission='read', password='guest')
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)