import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
import psycopg2
import urlparse

app=Flask(__name__)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

app.config['SQLALCHEMY_DATABASE_URI'] =  'postgres://vcatibplosonrr:Gy8S844p-JG4HeBUsNNZ_wq_lo@ec2-54-83-3-38.compute-1.amazonaws.com:5432/d7lr2ugo0d839c'
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/profilesdb"
heroku = Heroku(app)
db=SQLAlchemy(app)

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

from app import views, models
