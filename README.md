# GerenTAR

Sistema web para gerenciamento simples de tarefas, desenvolvido com Flask.

## Funcionalidades

- Criar conta e fazer login para acessar suas tarefas
- Adicionar novas tarefas com descrição e data de conclusão
- Visualizar tarefas pendentes e concluídas com estatísticas
- Marcar tarefas como concluídas ou reabri-las
- Excluir tarefas quando não forem mais necessárias
- Interface escura moderna com indicadores visuais de prazo

## Tecnologias

- **Backend:** Python, Flask, SQLAlchemy, Flask-Login, Flask-Migrate
- **Frontend:** HTML, CSS (tema escuro personalizado), Jinja2
- **Banco de dados:** SQLite (desenvolvimento)

## Como rodar

```bash
# Clone o repositório
git clone https://github.com/IsaacLusca/GerenTAR.git
cd GerenTAR

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Linux/Mac

# Instale as dependências
pip install -r requerements.txt

# Configure o banco de dados
flask db upgrade

# Crie o usuário de teste
flask seed

# Execute o servidor
python scripts.py
```

Acesse em: `http://localhost:5000`

## Usuário de teste

| Usuário | Senha |
|---------|-------|
| `teste` | `123`  |

> Você também pode criar uma nova conta na página de registro.

## Estrutura do projeto

```
GerenTAR/
├── app/
│   ├── static/css/style.css   # Estilos da interface
│   ├── templates/             # Templates Jinja2
│   │   ├── base.html          # Layout base
│   │   ├── index.html         # Dashboard de tarefas
│   │   ├── login.html         # Página de login
│   │   └── register.html      # Página de registro
│   ├── __init__.py            # Inicialização do app
│   ├── forms.py               # Formulários WTForms
│   ├── models.py              # Modelos do banco
│   └── routes.py              # Rotas da aplicação
├── migrations/                # Migrações do banco
├── scripts.py                 # Ponto de entrada
├── config.py                  # Configurações
└── requerements.txt           # Dependências
```
