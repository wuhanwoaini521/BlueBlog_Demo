'''
Author: han wu 
Date: 2021-12-25 20:15:28
LastEditTime: 2021-12-25 22:28:21
LastEditors: your name
Description: 自定义命令
FilePath: /BlueBlog_Demo/blueblog/commands.py
~~~~~~~~~吼吼吼~~~~~~~~~~
'''

import click
from blueblog.extensions import db

def register_commands(app):
    
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
        



    