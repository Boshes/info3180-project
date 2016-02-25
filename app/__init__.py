from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://testuser:password@localhost/profiledb"

db=SQLAlchemy(app)

from app import views, models
