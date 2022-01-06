'''
Author: han wu 
Date: 2021-12-23 09:37:49
LastEditTime: 2021-12-25 22:55:11
LastEditors: your name
Description:  虚拟数据
FilePath: /BlueBlog_Demo/blueblog/fakes.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''
from blueblog.models import Admin, Category, Post, Comment
from blueblog.extensions import db
from sqlalchemy.exc import IntegrityError

import random
from faker import Faker

# Faker 实例化
faker = Faker()

# 生成管理员信息
def fake_admin():
    admin = Admin(
		username = 'admin',
		blog_title = 'Blueblog',
		blog_sub_title = 'No, I\'m the real thing.',
		name = "Mima kirigoe",
		about = "Um, I, Mima Kirigor, had a fun time as a member of CHAM..."
	)
    admin.set_password("helloflask")
    db.session.add(admin)
    db.session.commit()
    
# 创建虚拟分类
def fake_categories(count = 10):
    category = Category(name = "Default")
    db.session.add(category)
    
    for i in range(count):
        category = Category(name = faker.word())
        db.session.add(category)
        
        # 因为在设计数据库得时候，规定了，分类名不能重复，所以在这做了异常捕获，重复得话就进行回滚，重新生成
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


# 生成虚拟文章
def fake_posts(count = 50):
    for i in range(count):
        post = Post(
			title = faker.sentence(),
			body = faker.text(2000),
			category = Category.query.get(random.randint(1, Category.query.count())), # 生成文章根据随机数，来选择进入那个分类下面
			timestamp = faker.date_time_this_year()
		)
        db.session.add(post)
    db.session.commit()

# 生成虚拟评论
def fake_comments(count = 500):
    for i in range(count):
        comment = Comment(
			author = faker.name(),
			email = faker.email(),
			site = faker.url(),
			body = faker.sentence(),
			timestamp = faker.date_time_this_year(),
			reviewed = True,
			post = Post.query.get(random.randint(1, Post.query.count()))
		)
        db.session.add(comment)
        
    salt = int(count * 0.1)
    for i in range(salt):
        # 未审核评论
        comment = Comment(
			author = faker.name(),
			email = faker.email(),
			site = faker.url(),
			body = faker.sentence(),
			timestamp = faker.date_time_this_year(),
			reviewed = True,
			post = Post.query.get(random.randint(1, Post.query.count()))
		) 
        db.session.add(comment)
        
        # 管理员发表得评论
        comment = Comment(
			author = "Mima Kirigoe",
			email = "mima@example.com",
			site = "example.com",
			body = faker.sentence(),
			timestamp = faker.date_time_this_year(),
			from_admin = True,
			reviewed = True,
			post = Post.query.get(random.randint(1, Post.query.count()))
		) 
        db.session.add(comment)
    db.session.commit()
    
    # 回复 ==> 需要评论生效才可以，要不然，如果评论还没提交得话，那么 评论得db是空的，就没有办法生成虚拟数据
    for i in range(salt):
        # 未审核评论
        comment = Comment(
			author = faker.name(),
			email = faker.email(),
			site = faker.url(),
			body = faker.sentence(),
			timestamp = faker.date_time_this_year(),
			reviewed = True,
			replied = Comment.query.get(random.randint(1, Comment.query.count()))
		) 
        db.session.add(comment)
    db.session.commit()