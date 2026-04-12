# ATV_LDW_API-FLASK
☕ Cafeteria
API REST para gerenciamento completo de uma cafeteria, incluindo controle de clientes, funcionários, produtos e pedidos. O projeto utiliza uma arquitetura modular com Blueprints e documentação automatizada com Swagger.

🛠️ Tecnologias Principais
Framework: Flask

Documentação: Flasgger (Swagger)

ORM/Banco de Dados: SQLAlchemy / SQLite

Containerização: Docker & Docker Compose

Ambiente: python-dotenv

🚀 Como Executar o projeto
A maneira mais rápida de rodar o projeto é utilizando o Docker, que já configura todo o ambiente necessário.

Passo a Passo
Clone o repositório:
git clone https://github.com/BDlucca/ATV_LDW_API-FLASK.git

Suba os containers:

No terminal rode:
docker-compose up -d

Acesse o backend:
cd apps/backend

Instale/atualize as dependências:
uv sync

Execute o migrations:
uv run alembic upgrade head

Inicie a aplicação Flask:
uv run flask --app src.app run


Acesse a aplicação:
API: http://localhost:5000

Swagger (Documentação): http://localhost:5000/apidocs/

📖 Documentação da API
A API foi documentada seguindo a especificação Swagger 2.0. Os principais recursos gerenciados são:

Clientes: GET/POST/PUT/DELETE em /api/cliente

Funcionários: GET/POST/PUT/DELETE em /api/funcionario

Produtos: GET/POST/PUT/DELETE em /api/produto

Pedidos: GET/POST/PUT/DELETE em /api/pedido