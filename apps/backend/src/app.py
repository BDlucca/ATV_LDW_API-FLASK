from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv
import os
from schemas.cliente_schema import ClienteSchema
from schemas.funcionario_schema import FuncionarioSchema
from schemas.pedido_schema import PedidoSchema
from schemas.produto_schema import ProdutoSchema

load_dotenv()

def create_app():
    app = Flask(__name__)

    from database import init_db
    init_db(app)

    db_url = os.getenv('DATABASE_URL', '')
    env_label = 'Supabase' if 'supabase' in db_url else 'Local (Docker)'

    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'ATV_LDW_API_FLASK',
        'uiversion': 3,
        'description': 'Sistema de uma cafeteria',
        'specs_route': '/apidocs/'
        
    }

    swagger_template = {
        "tags" : [
            {"name": "Cliente"},
            {"name": "Funcionario"},
            {"name": "Pedidos"},
            {"name": "Produtos"},
        ],
        "definitions": {
            "Cliente" : ClienteSchema.model_json_schema(),
            "Funcionario": FuncionarioSchema.model_json_schema(),
            "Pedido": PedidoSchema.model_json_schema(),
            "Produto": ProdutoSchema.model_json_schema(),
            "Error": {
                "type": "object",
                "properties": {"error": {"type": "string"}}
            }

        }
    }
    
    Swagger(app, template=swagger_template)

    # Espaço reservado para registrar Blueprints depois

    from routes.clientes import cliente_bp
    from routes.funcionarios import funcionario_bp
    from routes.pedidos import pedido_bp
    from routes.produtos import produto_bp
    # ...
    app.register_blueprint(cliente_bp, url_prefix='/api/cliente')
    app.register_blueprint(funcionario_bp, url_prefix='/api/funcionario')
    app.register_blueprint(pedido_bp, url_prefix='/api/pedido')
    app.register_blueprint(produto_bp, url_prefix='/api/produto')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)