from app import app, db
from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
import sqlalchemy as sa

@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = {'username': 'Isaac'}
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
        },
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Verifica se o usuário já está autenticado, se sim, redireciona para a página inicial (impede que volte para login)
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    
    # instanciando o formulário de login
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data)) 
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        # Verifica se existe um parâmetro 'next' na URL, se não existir, redireciona para a página inicial
        # O parâmetro 'next' é usado para redirecionar o usuário para a página que ele estava tentando acessar 
        # antes de ser redirecionado para a página de login.
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))