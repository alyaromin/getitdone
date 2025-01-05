from flask_sqlalchemy import SQLAlchemy

from app import db


class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), nullable=False)
  content = db.Column(db.String(1024), nullable=False)


