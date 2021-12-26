'''
Author: han wu 
Date: 2021-12-23 09:36:20
LastEditTime: 2021-12-25 21:47:29
LastEditors: your name
Description: 
FilePath: /BlueBlog_Demo/blueblog/blueprints/auth.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''
from flask import render_template, flash, redirect, url_for, Blueprint

auth_bp = Blueprint(
	"auth", __name__
)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template('auth/login.html')

@auth_bp.route("/logout")
def logout():
    return render_template('auth/logout.html')