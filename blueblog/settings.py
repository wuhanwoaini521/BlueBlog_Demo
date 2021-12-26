'''
Author: han wu 
Date: 2021-12-25 16:32:59
LastEditTime: 2021-12-25 23:23:28
LastEditors: your name
Description: 
FilePath: /BlueBlog_Demo/blueblog/settings.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('BLUEBLOG Admin', MAIL_USERNAME)

    BLUEBLOG_EMAIL = os.getenv('BLUEBLOG_EMAIL')
    BLUEBLOG_POST_PER_PAGE = 10
    BLUEBLOG_MANAGE_POST_PER_PAGE = 15
    BLUEBLOG_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    BLUEBLOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    BLUEBLOG_SLOW_QUERY_THRESHOLD = 1

    BLUEBLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    BLUEBLOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
