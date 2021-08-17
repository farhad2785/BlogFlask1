from flask import session, render_template, request, abort, flash
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin
from .utils import admin_only_view


@admin.route('/')
@admin_only_view
def index():
    return "Hello from Admin index!"


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
        return 'Login Successfully!'
    if session.get('role') == 1:
        return 'You are already logged in!'


    # session['name'] = 'Davood'
    # session.clear()
    # print(session.get('name'))
    # print(session)
    return render_template('admin/login.html', form = form) # ,title = 'Admin Login'
