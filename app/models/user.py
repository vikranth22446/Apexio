"""
User based models such as Users, Friends, Followers, UserRole.
"""
# coding=utf-8
import string
import re

from app import db


class Rules(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, unique=True)
    has = db.Column(db.String)
    equals = db.Column(db.String)
    begins_with = db.Column(db.String)
    extension = db.Column(db.String)
    regex = db.Column(db.String)
    delete_file = db.Column(db.Boolean)
    move_to = db.Column(db.String)

    def matches_rule(self, filename, extension):
        if self.has and self.has not in filename:
            return False
        if self.equals and self.equals != filename:
            return False
        if self.begins_with and not filename.startswith(self.begins_with):
            return False
        if self.extension and extension != self.extension:
            return False
        if self.regex and re.match(self.regex, filename + extension):
            return False
        return True

    def get_json(self):
        return {
            "id": self.id,
            "has": self.has,
            "equals": self.equals,
            "begins_with": self.begins_with,
            "extension": self.extension,
            "delete_file": self.delete_file,
            "move_to": self.move_to,
            "regex": self.regex
        }


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
