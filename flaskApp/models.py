from datetime import datetime
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskApp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    grievances = db.relationship('Grievance', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=600):
        s = Serializer(current_app.config['SECRET_KEY'] , expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8') 

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Grievance(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    category_grievance = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    grievance_image_file = db.Column(db.String(20), nullable='False', default='default.jpg')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    used_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Grievance('{self.category_grievance}', '{self.title}', '{self.content}', '{self.date_posted}')"
