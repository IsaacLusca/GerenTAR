# O módulo os é usado para interagir com o sistema operacional, como acessar variáveis de ambiente.
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Usada para proteger dados sensíveis, como cookies de sessão, e ataques CSRF
    # os.environ.get('SECRET_KEY') é usado para obter a chave secreta do ambiente, se não estiver definida, uma string padrão é usada.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Configuração do banco de dados, usando SQLAlchemy para ORM (Object-Relational Mapping)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')