# GerenTAR

Sistema web para gerenciamento de tarefas, desenvolvido com Flask.

## Funcionalidades

- Criar conta e fazer login para gerenciar suas tarefas
- Adicionar tarefas com descrição e data de conclusão
- Visualizar tarefas pendentes e concluídas com estatísticas
- Marcar como concluída, reabrir ou excluir tarefas
- Indicadores visuais de prazo (seguro, próximo, vencido)
- Tema claro e amigável

## Tecnologias

- **Backend:** Python, Flask, SQLAlchemy, Flask-Login, Flask-Migrate
- **Frontend:** HTML, CSS (tema claro personalizado), Jinja2
- **Banco de dados:** SQLite

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

# Popule com dados de exemplo (usuário + tarefas)
flask seed

# Execute o servidor
python scripts.py
```

Acesse em: `http://localhost:5000`

## Comandos úteis

| Comando | Descrição |
|---------|-----------|
| `flask seed` | Cria usuário teste + tarefas de exemplo |
| `flask reset` | Remove dados e recria do zero |
| `flask db upgrade` | Aplica migrações do banco |

## Usuário de teste

| Usuário | Senha |
|---------|-------|
| `teste` | `123`  |

> Você também pode criar uma nova conta na página de registro.

## Estrutura

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
│   ├── models.py              # Modelos User e Task
│   └── routes.py              # Rotas da aplicação
├── migrations/                # Migrações do banco
├── scripts.py                 # Ponto de entrada + comandos CLI
├── config.py                  # Configurações
└── requerements.txt           # Dependências
```
