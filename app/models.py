from . import db
from flask_login import UserMixin
from sqlalchemy import func


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.Column(db.String(150))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    blogs = db.relationship('Blog')
