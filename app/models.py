from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

# função para carregar o usuário com base no ID, para que comunique com o Flask-Login 
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

# userMixin é uma classe do Flask-Login que fornece métodos e propriedades para gerenciar a autenticação de usuários.
# sendo esses metodos e propriedades: is_authenticated, is_active, is_anonymous, get_id
class User(db.Model, UserMixin):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    tasks: so.WriteOnlyMapped['Task'] = so.relationship(
        back_populates='author')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    # set_password é um método que define a senha do usuário, gerando um hash seguro para armazená-la no banco de dados.
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Task(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    deadline: so.Mapped[datetime | None] = so.mapped_column(
        sa.DateTime(timezone=True), nullable=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)

    author: so.Mapped[User] = so.relationship(back_populates='tasks')
    status: so.Mapped[bool] = so.mapped_column(default=False)

    def __repr__(self):
        return '<Post {}>'.format(self.body)