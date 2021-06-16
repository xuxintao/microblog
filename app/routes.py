from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Xintao'}
    posts = [
        {
            'author': {'username': 'Xintao'},
            'body': 'Beautiful Day in Guangzhou!'
        },
        {
            'author': {'username': 'Mengchen'},
            'body': 'Long long ago!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
