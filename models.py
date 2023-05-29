"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """USER"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String,
                           nullable=False,)
    last_name = db.Column(db.String,
                          nullable=False)
    image_url = db.Column(db.String,
                          nullable=True)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")    

class Post(db.Model):
    """Blog post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.Text,
                      nullable=False)
    content = db.Column(db.Text,
                        nullable=False)
    created_at =db.Column(db.Datetime,
                          nullable=False,
                          default=datetime.datetime.now)
    user_id = db.Column(db.Integer,
                        db.Foreign_key('users.id'),
                        nullable=False)


def connect_db(app):
    """Connect to database"""
    
    db.app = app
    db.init_app(app)