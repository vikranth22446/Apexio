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


class Rules(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, unique=True)
    rule = db.Column(db.String(140))


def checkRule(fileString, name):
    if name in fileString:
        return True
    else:
        return False


# m = len(str1) n = len(str2)
def editDistance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)
    return 1 + min(editDistance(str1, str2, m, n - 1),  # Insert
                   editDistance(str1, str2, m - 1, n),  # Remove
                   editDistance(str1, str2, m - 1, n - 1)  # Replace
                   )


def removeExtension(fileNameString):
    last = 0
    for i in range(0, len(fileNameString)):
        if fileNameString[len(fileNameString) - i - 1] == '.':
            last = i
            break
    return fileNameString[:len(fileNameString) - last - 1]
