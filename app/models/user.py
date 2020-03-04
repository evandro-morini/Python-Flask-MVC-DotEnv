from app import db, ma, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    pwd = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, pwd):
        self.name = name
        self.email = email
        self.pwd = generate_password_hash(pwd)

    @property
    def password(self):
        raise AttributeError('Não é possível acessar a senha do usuário')

    def verify_password(self, pwd):
        return check_password_hash(self.pwd, pwd)

    def __repr__(self):
        return '<User: {}>'.format(self.name)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'pwd')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
