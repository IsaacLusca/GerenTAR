import os

class Config:
    # Usada para proteger dados sensíveis, como cookies de sessão, e ataques CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'