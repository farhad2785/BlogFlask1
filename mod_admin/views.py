from flask import session, render_template, request, abort
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin


@admin.route('/')
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
            return 'Incorrect Email', 400
        if not user.check_password(form.password.data):
            return 'Incorrect Password', 400
        session['email'] = user.email
        session['user_id'] = user.id
        # print(session)
        return 'Login Successfully!'
    if session.get('email') is not None:
        return 'You are already logged in!'


    # session['name'] = 'Davood'
    # session.clear()
    # print(session.get('name'))
    # print(session)
    return render_template('admin/login.html', form = form)
