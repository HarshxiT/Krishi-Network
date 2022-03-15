import datetime
from run import db
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry


class Post(db.Model):
   __tablename__ = 'post'
   id = db.Column(db.Integer(), primary_key = True)
   message = db.Column(db.String)
   location = db.Column(Geometry(geometry_type='POINT'))
   active = db.Column(db.Boolean, default=True)
   created_on = db.Column(db.DateTime, default=datetime.datetime.now(datetime.timezone.utc))

   def __init__(self, message,location=None):
      self.message = message
      self.location = location