from flask import render_template,redirect,url_for,flash
from app_package import app,mongo

@app.route("/",methods=["GET","POST"])
def index():
    