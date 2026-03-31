from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)

    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'ATV_LDW_API_FLASK',
        'uiversion': 3
    }
    Swagger(app)

    # Espaço reservado para registrar Blueprints depois

    from routes.bebidas import bebida_bp
    from routes.sobremesa import sobremesa_bp
    from routes.sanduiches import sanduiches_bp
    from routes.comand import comand_bp
    # ...
    app.register_blueprint(bebida_bp, url_prefix='/api/bebida')
    app.register_blueprint(sobremesa_bp, url_prefix='/api/sobremesa')
    app.register_blueprint(sanduiches_bp, url_prefix='/api/sanduiches')
    app.register_blueprint(comand_bp, url_prefix='/api/comand')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)