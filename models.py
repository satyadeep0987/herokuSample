import os
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from app import db

'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}