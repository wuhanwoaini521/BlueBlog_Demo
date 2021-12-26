'''
Author: han wu 
Date: 2021-12-23 09:36:26
LastEditTime: 2021-12-25 21:47:54
LastEditors: your name
Description: 
FilePath: /BlueBlog_Demo/blueblog/blueprints/admin.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''
from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, send_from_directory


admin_bp = Blueprint(
	"admin", __name__
)

