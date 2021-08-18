from flask import request, render_template, flash
from sqlalchemy.exc import IntegrityError
from app import db
from . import users
from .forms import Register_Form
from .models import User


@users.route('/register/', methods = ['GET' , 'POST'])
def register():
    form = Register_Form(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/register.html', form=form)
        if not form.password.data == form.confirm_password.data:
            error_msg = 'Password and Confirm Password does not match!'
            form.confirm_password.errors.append(error_msg)
        # اگر فیلدهای بیشتری برای یونیک بودن وجود داشته باشد نمی شود که از ترای استفاده کرد
        # و باید به شکل زیر اول یه کوری زد و سرچ کرد
        # find_user = User.query.filter(User.email.ilike(form.email.data)).first()
        # if find_user:
        #     flash('Email is in use.','Error')
        #     return render_template('users/register.html', form=form)
        new_user = User()
        new_user.full_name = form.full_name.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Your account was create successfully.','success')
        # except Exception
        except IntegrityError:
            db.session.rollback()
            flash('Email is in use.','Error')
    return render_template('users/register.html', form=form)