from app import db
from app.models.post import *
from app.models.blacklist import *
from app.models.user import *
from app.models.many_to_many import *

session = db.session
