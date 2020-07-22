from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

# Methods - tell what type of requests this page accepts (default get only)
# GET - the server returns data to the client
# POST - the client submits data to the server typically a form

@app.route('/login', methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    # When the browser submits a POST request the validate_on_submit() will check the forms validators
    if form.validate_on_submit():
        
        # Search the SQL data base for the user
        user = User.query.filter_by(username = form.username.data).first()

        # If the username is none or if the password hash did not match then leave them on the login
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))

        # If they match then log them in
        login_user(user, remember=form.remember_me.data)
        



        return redirect(url_for('index'))

    return render_template('login.html', title ='Sign In', form=form)


@app.route('/logout')
def logout()
    logout_user()
    return redirect(url_for('index')



@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Rebecca'}

    posts = [
        {
            'author': {'username': 'Rebecca'},
            'body': 'Test text 1'
        },
        {
            'author': {'username': 'Thomas'},
            'body': 'Test text 2'
        }
    ]


    return render_template('index.html',title = 'Home',user=user,posts=posts)



