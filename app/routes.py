from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember.data))
        # url_for para chamar como func no html
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)