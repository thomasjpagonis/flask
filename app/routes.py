from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# Methods - tell what type of requests this page accepts (default get only)
# GET - the server returns data to the client
# POST - the client submits data to the server typically a form

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    # When the browser submits a POST request the validate_on_submit() will check the forms validators
    if form.validate_on_submit():
        
        flash('Login reguested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title ='Sign In', form=form)


@app.route('/')
@app.route('/index')
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



