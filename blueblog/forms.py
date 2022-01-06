'''
Author: han wu 
Date: 2021-12-23 09:37:32
LastEditTime: 2022-01-02 10:24:52
LastEditors: your name
Description:  表单
FilePath: /BlueBlog_Demo/blueblog/forms.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, \
    SelectField, ValidationError, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Email, Optional, URL
from flask_ckeditor import CKEditorField

from blueblog.models import Category

# 登录表单
class LoginForm(FlaskForm):
    # 用户名，密码，复选框，提交按钮
    username = StringField("Username", validators = [DataRequired(), Length(1, 20)])
    password = PasswordField("Password", validators = [DataRequired(), Length(8, 128)])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in")

# 文章表单
class PostForm(FlaskForm):
    title = StringField("Title", validators = [DataRequired(), Length(1, 60)])
    category = SelectField('Category', coerce = int, default = 1) # coerce 指定数据类型为整型
    body = CKEditorField('Body', validators = [DataRequired()])
    submit = SubmitField()
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id , category.name) for category in Category.query.order_by(Category.name).all()]
		# choices 是SelectField自带得属性，用来指定 下拉列表选项（<option>标签）

# 分类创建表单
class CategoryForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired(), Length(1, 30)])
    submit = SubmitField()
    
    def validate_name(self, field):
        if Category.query.filter_by(name = field.data).first(): # field.name 用来获取用户输入得内容（分类名称）
            raise ValidationError("Name already in use.")
        
# 评论表单
class CommentForm(FlaskForm):
    author = StringField("Author", validators = [DataRequired(), Length(1, 30)])
    email = StringField("Email", validators = [DataRequired(), Length(1,254), Email()])
    site = StringField("Site", validators = [Optional(), URL(), Length(0,255)]) # Optional验证器使得字段可以为空
    body = TextAreaField("Comment", validators = [DataRequired()])
    submit = SubmitField()

# 管理员得评论表单
class AdminCommentForm(FlaskForm):
    author = HiddenField()
    email = HiddenField()
    site = HiddenField()
    
class SettingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    blog_title = StringField('Blog Title', validators=[DataRequired(), Length(1, 60)])
    blog_sub_title = StringField('Blog Sub Title', validators=[DataRequired(), Length(1, 100)])
    about = CKEditorField('About Page', validators=[DataRequired()])
    submit = SubmitField()
    

class LinkForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    url = StringField('URL', validators=[DataRequired(), URL(), Length(1, 255)])
    submit = SubmitField()