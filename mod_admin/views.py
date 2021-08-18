from app import db
from flask import (abort, flash, redirect, render_template, request, session,
                   url_for)
from sqlalchemy.exc import IntegrityError
from mod_blog.forms import CreatePostForm
from mod_blog.models import Post
from mod_users.forms import LoginForm
from mod_users.models import User

from . import admin
from .utils import admin_only_view


@admin.route('/')
@admin_only_view
def index():
    return render_template('admin/index.html')


@admin.route('/login/', methods = ['GET' , 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        # print(f'Form is validated!? {form.validate_on_submit()}')
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email == form.email.data).first()
        # user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
        # print(user)
        if not user:
            flash('Incorrect Email', category='Error')
            return render_template('admin/login.html', form = form) # ,title = 'Admin Login'
        if not user.check_password(form.password.data):
            flash('Incorrect Password', category='Error')
            return render_template('admin/login.html', form = form) # ,title = 'Admin Login'
        # if not user.is_admin():
        #     flash('Sorry! You are not admin', category='Warning')
        #     return render_template('admin/login.html', form = form) # ,title = 'Admin Login'
        session['email'] = user.email
        session['user_id'] = user.id
        session['role'] = user.role
        # print(session)
        return redirect(url_for('admin.index'))
    if session.get('role') == 1:
        return redirect(url_for('admin.index'))


    # session['name'] = 'Davood'
    # session.clear()
    # print(session.get('name'))
    # print(session)
    return render_template('admin/login.html', form = form) # ,title = 'Admin Login'

@admin.route('/logout/', methods = ['GET'])
@admin_only_view
def logout():
    session.clear()
    flash('You logged out successfuly!','Warning')
    return redirect(url_for('admin.login'))

@admin.route('/posts/new', methods = ['GET' , 'POST'])
@admin_only_view
def create_post():
    form = CreatePostForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return 'not validate'
        new_post = Post()
        new_post.title = form.title.data
        new_post.content = form.content.data
        new_post.slug = form.slug.data
        new_post.summary = form.summary.data
        try:
            db.session.add(new_post)
            db.session.commit()
            flash('Post created!')
            return redirect(url_for('admin.index'))
        # except Exception as e:
        except IntegrityError:
            db.session.rollback()

    return render_template('admin/create_post.html', form = form)
