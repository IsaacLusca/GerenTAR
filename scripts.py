from app import app, db
from app.models import User

@app.cli.command('seed')
def seed():
    """Cria um usuário de teste no banco de dados."""
    if User.query.filter_by(username='teste').first():
        print('Usuário teste já existe.')
        return
    user = User(username='teste', email='teste@email.com')
    user.set_password('123')
    db.session.add(user)
    db.session.commit()
    print('Usuário teste criado: teste / 123')

if __name__ == '__main__':
    app.run(debug=True)
