from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, permission='read', password=None):
        self.id = id
        self.password = password
        self.permission = permission

users = {
    'admin': User('admin', 'edit', 'admin'),
    'user': User('user', 'download', 'user'),
    'guest': User('guest', 'read', 'guest')
}