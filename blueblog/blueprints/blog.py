'''
Author: han wu 
Date: 2021-12-23 09:36:13
LastEditTime: 2021-12-26 09:24:41
LastEditors: your name
Description: auth.
FilePath: /BlueBlog_Demo/blueblog/blueprints/blog.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''

from flask import render_template, Blueprint,request,current_app
from blueblog.models import Post


blog_bp = Blueprint(
	'blog', __name__
)

@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BLUEBLOG_POST_PER_PAGE'] # 因为create_app配置成了工厂函数，所以得话就需要使用current_app.config得方式来调用配置好的config文件
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('blog/index.html', posts = posts, pagination = pagination)

@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')

@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    return render_template('blog/category.html')

@blog_bp.route('/post/<int:post_id>', methods=['GET','POST'])
def show_post(post_id):
    return render_template('blog/post.html')