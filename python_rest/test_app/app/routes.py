from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect("/index")
        #return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/test')
def test():
    return render_template('test.html')