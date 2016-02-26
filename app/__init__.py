import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://xcismaysusivmw:l-ZuQFltgx54-zd5FMATK3uxRI@ec2-54-83-3-38.compute-1.amazonaws.com:5432/ddujna1vdv7ctd"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/profilesdb"

db=SQLAlchemy(app)

from app import views, models
