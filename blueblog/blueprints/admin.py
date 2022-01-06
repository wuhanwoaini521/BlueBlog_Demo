'''
Author: han wu 
Date: 2021-12-23 09:36:26
LastEditTime: 2022-01-02 10:27:56
LastEditors: your name
Description: 
FilePath: /BlueBlog_Demo/blueblog/blueprints/admin.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''
import os

from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, send_from_directory
from flask_login import login_required, current_user
from flask_ckeditor import upload_success, upload_fail

from blueblog.extensions import db
from blueblog.forms import SettingForm, PostForm, CategoryForm, LinkForm
from blueblog.models import Post, Category, Comment
from blueblog.utils import redirect_back, allowed_file

admin_bp = Blueprint(
	"admin", __name__
)



@admin_bp.route('/post/<int:post_id>/set-comment', methods=['POST'])
@login_required
def set_comment(post_id):
    post = Post.query.get_or_404(post_id)
    if post.can_comment:
        post.can_comment = False
        flash('Comment disabled.', 'success')
    else:
        post.can_comment = True
        flash('Comment enabled.', 'success')
    db.session.commit()
    return redirect_back()

@admin_bp.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted.', 'success')
    return redirect_back()