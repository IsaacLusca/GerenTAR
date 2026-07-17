# GerenTAR

Sistema web para gerenciamento de tarefas, desenvolvido com Flask.

🌐 **Deploy:** [https://gerentar.onrender.com](https://gerentar.onrender.com)

## Funcionalidades

- Criar conta e fazer login para gerenciar suas tarefas
- Adicionar tarefas com descrição e data de conclusão
- Visualizar tarefas pendentes e concluídas com estatísticas
- Marcar como concluída, reabrir ou excluir tarefas
- Indicadores visuais de prazo (seguro, próximo, vencido)
- Tema claro e amigável

## Tecnologias

- **Backend:** Python, Flask, SQLAlchemy, Flask-Login
- **Frontend:** HTML, CSS, Jinja2
- **Banco de dados:** SQLite (desenvolvimento) / PostgreSQL (produção)

## Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/IsaacLusca/GerenTAR.git
cd GerenTAR

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor (cria tabelas e seed automaticamente)
python scripts.py
```

Acesse em: `http://localhost:5000`

## Usuário de teste

| Usuário | Senha |
|---------|-------|
| `teste` | `123`  |

> Você também pode criar uma nova conta na página de registro.

## Deploy no Render

O deploy é automático via `render.yaml`. A cada push na branch `main`:

1. Render instala as dependências
2. Gunicorn inicia o app
3. Tabelas e seed são criados automaticamente na inicialização

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
│   ├── __init__.py            # Inicialização do app + seed automático
│   ├── forms.py               # Formulários WTForms
│   ├── models.py              # Modelos User e Task
│   └── routes.py              # Rotas da aplicação
├── .python-version            # Versão do Python (Render)
├── render.yaml                # Configuração de deploy
├── render_start.sh            # Script de inicialização
├── scripts.py                 # Ponto de entrada + comandos CLI
├── config.py                  # Configurações
└── requirements.txt           # Dependências
```
