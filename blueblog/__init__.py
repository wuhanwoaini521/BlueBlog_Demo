'''
Author: han wu 
Date: 2021-12-23 09:37:27
LastEditTime: 2022-01-02 10:26:55
LastEditors: your name
Description: 
FilePath: /BlueBlog_Demo/blueblog/__init__.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''

import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler

import click
from flask import Flask, render_template, request
from flask_login import current_user
from flask_sqlalchemy import get_debug_queries
from flask_wtf.csrf import CSRFError

from blueblog.settings import config
from blueblog.extensions import bootstrap, db, ckeditor, mail, moment, login_manager,csrf
from blueblog.blueprints.admin import admin_bp
from blueblog.blueprints.auth import auth_bp
from blueblog.blueprints.blog import blog_bp
from blueblog.models import Admin, Post, Category, Comment

# from blueblog.commands import register_commands

from blueblog.models import Admin, Category

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name = None): # 配置FLASK_APP应用后，会自动检测一个应用或者工厂（create_app）
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development') #  加载配置
        
    app = Flask('blueblog')
    app.config.from_object(config[config_name])
    app.secret_key = 'xxxxyyyyyzzzzz'
    
    register_logging(app) # 注册日志处理器
    register_extensions(app) # 注册扩展（扩展初始化）
    register_blueprints(app) # 注册蓝本
    register_commands(app) # 注册自定义shell命令
    register_errors(app) # 注册错误处理函数
    register_shell_context(app) # 注册shell上下文处理函数
    register_template_context(app) # 注册模板上下文处理函数
    
    return app
    
def register_logging(app):
    pass

def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)

def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')

# 注册shell上下文处理函数
def register_shell_context(app):
    @app.shell_context_processor # 上下文处理器，返回字典中的键可以在模板上下文中使用
    def make_shell_context():
        return dict(db=db, Admin = Admin, Post = Post, Category = Category, Comment = Comment)
    
# 注册模板上下文处理函数
def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        # links = Link.query.order_by(Link.name).all()
        if current_user.is_authenticated:
            unread_comments = Comment.query.filter_by(reviewed=False).count()
        else:
            unread_comments = None
        return dict(
            admin=admin, categories=categories,
            unread_comments=unread_comments)

# 注册错误处理函数
def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400

# 注册自定义命令
def register_commands(app):
    
    # 自定义生成虚拟数据得函数
    @app.cli.command()
    @click.option('--category', default=10, help = "Quantitly of catefgories, default is 10.")
    @click.option('--post', default=50, help = "Quantitly of posts, default is 50.")
    @click.option('--comment', default=500, help = "Quantitly of comments, default is 500.")
    def forge(category, post, comment):
        from blueblog.fakes import fake_admin, fake_categories, fake_posts, fake_comments
        
        db.drop_all()
        db.create_all()
        
        click.echo('Generating the administrator...') 
        fake_admin() 
        
        click.echo('Generating %d categories...' % category) 
        fake_categories(category) 
        
        click.echo('Generating %d posts...' % post) 
        fake_posts(post) 
        
        click.echo('Generating %d comments...' % comment) 
        fake_comments(comment) 
        
        click.echo('Done.')
        
    # 自定义 更新数据得方法
    def initdb():
        pass