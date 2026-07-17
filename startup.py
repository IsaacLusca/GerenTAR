from app import app, db
from app.models import User, Task

with app.app_context():
    db.create_all()
    user = User.query.filter_by(username='teste').first()
    if not user:
        user = User(username='teste', email='teste@email.com')
        user.set_password('123')
        db.session.add(user)
        db.session.commit()
        print('Usuário teste criado: teste / 123')
    else:
        print('Usuário teste já existe.')

    if not Task.query.filter_by(author=user).first():
        from scripts import criar_tarefas_exemplo
        criar_tarefas_exemplo(user)
    else:
        print('Tarefas já existem.')
