from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Isaac'}
    posts = [
        {
            'autor': {'username': 'John'},
            'body': 'Bela manhã!'
        },
        {
            'autor': {'username': 'Susan'},
            'body': 'Amanhã é sexta-feira!'
        },
        {
            'autor': {'username': 'Mary'},
            'body': 'Vamos ao cinema?'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)