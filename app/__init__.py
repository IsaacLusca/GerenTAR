from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from flask_login import LoginManager

# O módulo os é usado para interagir com o sistema operacional, como acessar variáveis de ambiente.
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# flask_login é uma extensão para auxiliar na implementação de login de usuários
login = LoginManager(app)
login.login_view = 'login'  # Define a view para redirecionar quando o usuário não estiver autenticado


# models serve para definir as classes que representam as tabelas do banco de dados
from app import routes, models

with app.app_context():
    db.create_all()
    from app.models import User, Task
    from datetime import datetime, timedelta

    user = User.query.filter_by(username='teste').first()
    if not user:
        user = User(username='teste', email='teste@email.com')
        user.set_password('123')
        db.session.add(user)
        db.session.commit()

    if not Task.query.filter_by(author=user).first():
        today = datetime.utcnow()
        tarefas = [
            Task(body='Revisar relatório mensal', deadline=today + timedelta(days=5), author=user, status=False),
            Task(body='Comprar material de escritório', deadline=today + timedelta(days=1), author=user, status=False),
            Task(body='Responder e-mails pendentes', deadline=today - timedelta(days=2), author=user, status=False),
            Task(body='Preparar apresentação da equipe', deadline=today + timedelta(days=10), author=user, status=False),
            Task(body='Atualizar documentação do projeto', deadline=today + timedelta(days=3), author=user, status=False),
            Task(body='Organizar reunião com cliente', deadline=None, author=user, status=False),
            Task(body='Limpar caixa de entrada', deadline=today - timedelta(days=5), author=user, status=True),
            Task(body='Elaborar orçamento trimestral', deadline=today - timedelta(days=3), author=user, status=True),
            Task(body='Atualizar planilha de horas', deadline=today - timedelta(days=7), author=user, status=True),
            Task(body='Enviar relatório de despesas', deadline=today - timedelta(days=10), author=user, status=True),
        ]
        for i, t in enumerate(tarefas):
            t.timestamp = today - timedelta(days=15 - i)
        db.session.add_all(tarefas)
        db.session.commit()
