"""
User based models such as Users, Friends, Followers, UserRole.
"""
# coding=utf-8

from app import db
from app.utils.base_model import Model


class User(Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String, nullable=True, unique=True)
    social_type = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=True)
