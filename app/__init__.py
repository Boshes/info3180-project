import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'postgres://vcatibplosonrr:Gy8S844p-JG4HeBUsNNZ_wq_lo@ec2-54-83-3-38.compute-1.amazonaws.com:5432/d7lr2ugo0d839c'
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/profilesdb"
db=SQLAlchemy(app)
db.create_all()

from app import views, models
