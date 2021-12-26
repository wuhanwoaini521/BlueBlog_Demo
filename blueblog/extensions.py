'''
Author: han wu 
Date: 2021-12-23 09:37:54
LastEditTime: 2021-12-24 21:29:17
LastEditors: your name
Description: 扩展
FilePath: /BlueBlog_Demo/blueblog/extensions.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''

from flask_bootstrap import Bootstrap # 导入样式
from flask_sqlalchemy import SQLAlchemy # 使用数据库
from flask_mail import Mail # 使用邮件
from flask_ckeditor import CKEditor # 使用富文本编辑器
from flask_moment import Moment # 本地化

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()

