from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate   

# O módulo os é usado para interagir com o sistema operacional, como acessar variáveis de ambiente.
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models serve para definir as classes que representam as tabelas do banco de dados
from app import routes, models
