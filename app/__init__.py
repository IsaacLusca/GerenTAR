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
