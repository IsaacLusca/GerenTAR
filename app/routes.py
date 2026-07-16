from datetime import datetime, timezone
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from urllib.parse import urlsplit
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Task
import sqlalchemy as sa
from app.forms import RegistrationForm, SubmitTaskForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # user = {'username': 'Isaac'}
    # posts = [
    #     {
    #         'autor': {'username': 'John'},
    #         'body': 'Bela manhã!'
    #     },
    #     {
    #         'autor': {'username': 'Susan'},
    #         'body': 'Amanhã é sexta-feira!'
    #     },
    #     {
    #         'autor': {'username': 'Mary'},
    #         'body': 'Vamos ao cinema?'
    #     },
    # ]
    form = SubmitTaskForm()
    if form.validate_on_submit():
        # Cria uma nova tarefa com os dados do formulário
        task = Task(body=form.body.data, deadline=form.deadline.data, author=current_user)
        # Adiciona a nova tarefa à sessão do banco de dados e faz o commit para salvar as alterações
        db.session.add(task)
        db.session.commit()
        flash('Tarefa adicionada com sucesso!', 'success')
        return redirect(url_for('index'))
    
    # Busca todas as tarefas do usuário atual
    posts = Task.query.filter_by(author=current_user, status=False).all()
    posts_check = Task.query.filter_by(author=current_user, status=True).all()
    return render_template('index.html', title='Home', form=form, posts=posts, posts_check=posts_check, utcnow=datetime.now(timezone.utc))

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
            flash('Usuário ou senha inválidos', 'warning')
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Verifica se o usuário já está autenticado, se sim, redireciona para a página inicial (impede que volte para login)
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # instanciando o formulário de registro
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # Cria um novo usuário com os dados do formulário
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        # Adiciona o novo usuário à sessão do banco de dados e faz o commit para salvar as alterações
        db.session.add(user)
        db.session.commit()
        flash('Você foi registrado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registrar', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/task/<int:task_id>/complete', methods=['POST'])
@login_required
def complete_task(task_id):
    # Busca a tarefa pelo ID e verifica se pertence ao usuário atual
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    task.status = True  # Atualiza o status para True
    db.session.commit()  # Salva as alterações no banco de dados
    flash('Tarefa marcada como concluída!', 'success')
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/incomplete', methods=['POST'])
@login_required
def incomplete_task(task_id):
    # Busca a tarefa pelo ID e verifica se pertence ao usuário atual
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    task.status = False  # Atualiza o status para True
    db.session.commit()  # Salva as alterações no banco de dados
    flash('Tarefa marcada como incompleta!', 'warning')
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    # Busca a tarefa pelo ID e verifica se pertence ao usuário atual
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(task)  # Remove a tarefa do banco de dados
    db.session.commit()  # Salva as alterações no banco de dados
    flash('Tarefa deletada com sucesso!', 'success')
    return redirect(url_for('index'))