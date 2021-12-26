'''
Author: han wu 
Date: 2021-12-23 09:37:37
LastEditTime: 2021-12-25 22:52:49
LastEditors: your name
Description: 
FilePath: /BlueBlog_Demo/blueblog/models.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''
from sqlalchemy.orm import backref
from blueblog.extensions import db
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


# 管理员模型
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 主键
    username = db.Column(db.String(20)) 
    password_hash = db.Column(db.String(128)) # 密码散列值
    blog_title = db.Column(db.String(60)) # 博客标题
    blog_sub_title = db.Column(db.String(100)) # 博客副标题
    name = db.Column(db.String(30)) # 用户姓名
    about = db.Column(db.Text) # 关于信息
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

# 分类 
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique=True) # 分类名，不允许重复，使用unique = True
    
    # 一对多关系，一个分类下面有多个文章
    posts = db.relationship('Post', back_populates = 'category')

# 文章
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 一对多关系，一个分类下面有多个文章
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates = "posts")
    
    # 一对多关系，一篇文章下有多条评论
    comments = db.relationship('Comment', back_populates = "post", cascade = "all, delete-orphan")
    
    
# 评论
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(254))
    site = db.Column(db.String(255))
    body = db.Column(db.Text)
    from_admin = db.Column(db.Boolean, default=False) # 用来判断是否是管理员得评论，默认为false
    reviewed = db.Column(db.Boolean, default=False) # 判断评论是否通过审核
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index = True)
    
    # 一对多关系，一篇文章下有多条评论
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates = 'comments')
    
    # 邻接列表关系
    replied_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    replied = db.relationship('Comment', back_populates = 'replies', remote_side = [id])
    replies = db.relationship('Comment', back_populates = 'replied', cascade = "all")
