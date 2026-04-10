# Sistema de Encargos - Academic Workload Management System

A Django-based web application for managing and tracking academic teaching assignments (encargos) and calculating professor workload balance.

## Overview

This system helps educational institutions manage and monitor professional teaching assignments, track workload hours, calculate average points per semester, and maintain balance records for each professor.

## Features

- **Professor Management**: Add and manage professor profiles
- **Workload Tracking**: Record teaching assignments with hours and points
- **Balance Calculation**: Automatically compute workload balance (hours vs. assignments)
- **Semester Analysis**: Track workload by year and semester (half-year periods)
- **Average Calculation**: Calculate average points per semester across all professors
- **Historical Records**: Maintain historical data for auditing and analysis

## Technology Stack

- **Framework**: Django (Python web framework)
- **Database**: SQLite3
- **Frontend**: HTML/CSS templates
- **Python**: 2.7+ (as evidenced by `__unicode__` methods)

## Project Structure

```
sistema_encargos/
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── projeto/                   # Main project configuration
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI configuration
├── saldo/                     # Main application
│   ├── models.py             # Data models (Professor, Encargo, Media)
│   ├── views.py              # View handlers
│   ├── forms.py              # Form definitions
│   ├── admin.py              # Django admin configuration
│   ├── tests.py              # Unit tests
│   └── migrations/           # Database migrations
├── templates/                 # HTML templates
│   └── saldo/
│       ├── index.html        # Main dashboard
│       ├── addprof.html      # Add professor form
│       ├── addencargo.html   # Add workload assignment form
│       ├── calcularmedia.html # View calculated averages
│       └── versaldo.html     # View balance details
└── static/                    # Static files
    └── css/
        └── style.css         # Stylesheet

```

## Data Models

### Professor
- `nome` (CharField, max 60 chars): Professor name

### Encargo
- `professor` (ForeignKey): Reference to Professor
- `ano` (CharField): Academic year
- `sem` (CharField): Semester (1 or 2)
- `horas` (FloatField): Hours of work
- `encargos` (FloatField): Teaching assignments count
- `pontos` (FloatField): Calculated points (encargos - horas)
- `saldo_i` (FloatField): Initial balance
- `saldo_f` (FloatField): Final balance

### Media
- `somapt` (FloatField): Sum of points
- `nelementos` (IntegerField): Number of elements
- `media` (FloatField): Calculated average
- `anosem` (CharField): Year/Semester reference

## URL Routes

| Route | Function | Purpose |
|-------|----------|---------|
| `/index/` | index | Display main dashboard with professors and assignments |
| `/addprof/` | addprof | Add new professor |
| `/addencargo/` | addencargo | Add new teaching assignment |
| `/calcularmedia/` | calcularmedia | Calculate and display averages |
| `/saldo/` | saldo | View balance information |
| `/versaldo/<year>/<semster>/` | versaldo | View detailed balance for specific period |
| `/admin/` | Django Admin | Administrative interface |

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd sistema_encargos
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Main app: http://localhost:8000/index/
   - Admin panel: http://localhost:8000/admin/

## Usage

1. **Add Professors**: Navigate to `/addprof/` to add professor profiles
2. **Add Assignments**: Go to `/addencargo/` to record teaching assignments with hours
3. **Calculate Averages**: Visit `/calcularmedia/` to compute semester averages
4. **View Balance**: Check `/saldo/` or `/versaldo/<year>/<semester>/` to see workload balance
5. **Admin Management**: Use `/admin/` for direct database management

## Key Calculations

- **Points**: `encargos - horas` (Teaching assignments minus hours worked)
- **Average**: Total points divided by number of professors per semester
- **Balance**: Tracks initial and final balance across semesters

## Requirements

- Python 2.7+
- Django 1.x
- SQLite3 (included)

## Notes

- **Security**: The current settings have `DEBUG = True` and `ALLOWED_HOSTS = []`. Before deploying to production, update these settings in `settings.py`
- **Secret Key**: The SECRET_KEY is visible in settings.py - generate a new one for production
- **Database**: Uses SQLite, suitable for development; consider PostgreSQL/MySQL for production

## License

[Add your license information here]

## Author

[Add author information here]

## Support

For issues or questions, please [add contact information or issue tracker URL]


# 🇧🇷 Sistema de Encargos - Sistema de Gerenciamento de Carga Horária Acadêmica

Uma aplicação web baseada em Django para gerenciar e rastrear atribuições de ensino acadêmico (encargos) e calcular o equilíbrio de carga de trabalho dos professores.

## Visão Geral

Este sistema ajuda instituições educacionais a gerenciar e monitorar atribuições profissionais de ensino, rastrear horas de trabalho, calcular pontos médios por semestre e manter registros de saldo para cada professor.

## Funcionalidades

- **Gerenciamento de Professores**: Adicionar e gerenciar perfis de professores
- **Rastreamento de Carga Horária**: Registrar atribuições de ensino com horas e pontos
- **Cálculo de Saldo**: Calcular automaticamente o saldo de carga de trabalho (horas vs. atribuições)
- **Análise por Semestre**: Rastrear carga de trabalho por ano e semestre
- **Cálculo de Média**: Calcular pontos médios por semestre em todos os professores
- **Registros Históricos**: Manter dados históricos para auditoria e análise

## Stack Tecnológico

- **Framework**: Django (framework web Python)
- **Banco de Dados**: SQLite3
- **Frontend**: Templates HTML/CSS
- **Python**: 2.7+ (evidenciado pelos métodos `__unicode__`)

## Estrutura do Projeto

```
sistema_encargos/
├── db.sqlite3                 # Banco de dados SQLite
├── manage.py                  # Script de gerenciamento Django
├── projeto/                   # Configuração principal do projeto
│   ├── __init__.py
│   ├── settings.py           # Configurações do Django
│   ├── urls.py               # Roteamento de URLs
│   └── wsgi.py               # Configuração WSGI
├── saldo/                     # Aplicação principal
│   ├── models.py             # Modelos de dados (Professor, Encargo, Media)
│   ├── views.py              # Manipuladores de visualização
│   ├── forms.py              # Definições de formulários
│   ├── admin.py              # Configuração do admin Django
│   ├── tests.py              # Testes unitários
│   └── migrations/           # Migrações de banco de dados
├── templates/                 # Templates HTML
│   └── saldo/
│       ├── index.html        # Painel principal
│       ├── addprof.html      # Formulário de adição de professor
│       ├── addencargo.html   # Formulário de adição de atribuição
│       ├── calcularmedia.html # Visualizar médias calculadas
│       └── versaldo.html     # Visualizar detalhes de saldo
└── static/                    # Arquivos estáticos
    └── css/
        └── style.css         # Folha de estilos

```

## Modelos de Dados

### Professor
- `nome` (CharField, máx 60 caracteres): Nome do professor

### Encargo
- `professor` (ForeignKey): Referência ao Professor
- `ano` (CharField): Ano acadêmico
- `sem` (CharField): Semestre (1 ou 2)
- `horas` (FloatField): Horas trabalhadas
- `encargos` (FloatField): Quantidade de atribuições de ensino
- `pontos` (FloatField): Pontos calculados (encargos - horas)
- `saldo_i` (FloatField): Saldo inicial
- `saldo_f` (FloatField): Saldo final

### Media
- `somapt` (FloatField): Soma de pontos
- `nelementos` (IntegerField): Número de elementos
- `media` (FloatField): Média calculada
- `anosem` (CharField): Referência de ano/semestre

## Rotas de URL

| Rota | Função | Propósito |
|------|--------|----------|
| `/index/` | index | Exibir painel principal com professores e atribuições |
| `/addprof/` | addprof | Adicionar novo professor |
| `/addencargo/` | addencargo | Adicionar nova atribuição de ensino |
| `/calcularmedia/` | calcularmedia | Calcular e exibir médias |
| `/saldo/` | saldo | Ver informações de saldo |
| `/versaldo/<ano>/<semestre>/` | versaldo | Ver saldo detalhado para período específico |
| `/admin/` | Django Admin | Interface administrativa |

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositório>
   cd sistema_encargos
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install django
   ```

4. **Execute as migrações**:
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário** (para acesso ao admin):
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação**:
   - Aplicação principal: http://localhost:8000/index/
   - Painel de admin: http://localhost:8000/admin/

## Uso

1. **Adicionar Professores**: Navegue até `/addprof/` para adicionar perfis de professores
2. **Adicionar Atribuições**: Vá para `/addencargo/` para registrar atribuições de ensino com horas
3. **Calcular Médias**: Visite `/calcularmedia/` para calcular médias por semestre
4. **Ver Saldo**: Confira `/saldo/` ou `/versaldo/<ano>/<semestre>/` para ver o saldo de carga de trabalho
5. **Gerenciamento Admin**: Use `/admin/` para gerenciamento direto do banco de dados

## Cálculos Principais

- **Pontos**: `encargos - horas` (Atribuições de ensino menos horas trabalhadas)
- **Média**: Total de pontos dividido pelo número de professores por semestre
- **Saldo**: Rastreia saldo inicial e final em todos os semestres

## Requisitos

- Python 2.7+
- Django 1.x
- SQLite3 (incluído)

## Notas Importantes

- **Segurança**: As configurações atuais têm `DEBUG = True` e `ALLOWED_HOSTS = []`. Antes de implantar em produção, atualize essas configurações em `settings.py`
- **Chave Secreta**: A SECRET_KEY está visível em settings.py - gere uma nova para produção
- **Banco de Dados**: Usa SQLite, adequado para desenvolvimento; considere PostgreSQL/MySQL para produção

## Licença

[Adicione suas informações de licença aqui]

## Autor

[Adicione informações do autor aqui]

## Suporte

Para dúvidas ou problemas, por favor [adicione informações de contato ou URL do rastreador de problemas]
