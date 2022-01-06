'''
Author: han wu 
Date: 2021-12-23 09:37:54
LastEditTime: 2022-01-02 10:27:23
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
from flask_login import LoginManager # 
from flask_wtf import CSRFProtect


bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    from blueblog.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message = 'Your custom message'
login_manager.login_message_category = "warning"