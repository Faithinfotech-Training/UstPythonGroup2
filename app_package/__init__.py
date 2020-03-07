from flask import Flask
from flask_pymongo import PyMongo
from app_package.config import Config


app=Flask(__name__)

app.config.from_object(Config)
mongo=PyMongo(app)
from app_package import resroutes,croutes,routes