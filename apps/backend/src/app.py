from flask import Flask
from flasgger import Swagger
import os
from dotenv import load_dotenv
from database import init_db, db



from schemas.cliente_schema import ClienteSchema
from schemas.funcionario_schema import FuncionarioSchema
from schemas.pedido_schema import PedidoSchema
from schemas.produto_schema import ProdutoSchema

load_dotenv()

def create_app():
    app = Flask(__name__)
    init_db(app)
   
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de uma Cafeteria",
            "description": "API para gerenciar uma Cafeteria",
            "version": "1.0.0"
        },
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

    from routes.clientes import cliente_bp
    from routes.funcionarios import funcionario_bp
    from routes.pedidos import pedido_bp
    from routes.produtos import produto_bp

    app.register_blueprint(cliente_bp, url_prefix='/api/cliente')
    app.register_blueprint(funcionario_bp, url_prefix='/api/funcionario')
    app.register_blueprint(pedido_bp, url_prefix='/api/pedido')
    app.register_blueprint(produto_bp, url_prefix='/api/produto')

    return app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)