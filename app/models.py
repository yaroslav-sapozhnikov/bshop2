from app import db
from datetime import datetime
from flask_security import UserMixin, RoleMixin


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Post id: {self.id}, Post title: {self.title}'


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    confirmed_at = db.Column(db.DateTime())


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))


class Record(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    mobile = db.Column(db.String(20))
    service = db.Column(db.String(100))
    time = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Record, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Record id: {self.id}, time: {self.time}, service: {self.service}'
