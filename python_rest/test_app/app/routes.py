from flask import render_template
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
#return render_template('index.html', user=user)
#return render_template('index.html', title='Home',user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/test')
def test():
    return render_template('test.html')