from datetime import datetime, timedelta
from app import app, db
from app.models import User, Task

def criar_tarefas_exemplo(user):
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
    print(f'{len(tarefas)} tarefas de exemplo criadas.')

@app.cli.command('seed')
def seed():
    """Popula o banco com dados de exemplo."""
    user = User.query.filter_by(username='teste').first()
    if not user:
        user = User(username='teste', email='teste@email.com')
        user.set_password('123')
        db.session.add(user)
        db.session.commit()
        print('Usuário teste criado: teste / 123')
    else:
        print('Usuário teste já existe.')

    if Task.query.filter_by(author=user).first():
        print('Tarefas já existem. Use "flask reset" para recriar.')
        return

    criar_tarefas_exemplo(user)

@app.cli.command('reset')
def reset():
    """Remove dados e recria do zero."""
    Task.query.delete()
    User.query.filter(User.username != 'teste').delete()
    db.session.commit()
    user = User.query.filter_by(username='teste').first()
    if not user:
        user = User(username='teste', email='teste@email.com')
        user.set_password('123')
        db.session.add(user)
        db.session.commit()
        print('Usuário teste criado: teste / 123')
    criar_tarefas_exemplo(user)
    print('Banco resetado e populado novamente.')

if __name__ == '__main__':
    app.run(debug=True)
