from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm, DataForm
from flask_login import current_user, login_user
from app.models import User, Data
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'ShyGuy'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Test-Man'},
            'body': 'Everything is okay meow!'
        },
        {
            'author': {'username': 'Test-Man'},
            'body': 'Everything is okay meow!'
        },
        {
            'author': {'username': 'Test-Man'},
            'body': 'Everything is okay meow!'
        },
        {
            'author': {'username': 'Test-Man'},
            'body': 'Everything is okay meow!'
        }
    ]
    return render_template('index.html', title='Home Page', posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        #return redirect("/index")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/test')
def test():
    return render_template('test.html')
    #return redirect(url_for('test'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/data', methods=['GET', 'POST'])
def data():
    form = DataForm()
    return render_template('data.html', title='Data', form=form)

@app.route('/data_output', methods=['GET', 'POST'])
def data_output():
    #form = DataForm()

    return render_template('output.html', title="Data Output")#, form=form)
        #return redirect(url_for('output'))

