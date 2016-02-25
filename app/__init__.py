from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://qiuxgxiwedfala:iMUAzdx4siRlwJX0czJ7ti09EV@ec2-54-83-3-38.compute-1.amazonaws.com:5432/d97q1alb9u6ejs"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://testuser:password@localhost/profiledb"

db=SQLAlchemy(app)

from app import views, models
