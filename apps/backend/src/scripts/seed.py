import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv
load_dotenv()

from src.app import create_app
from src.database import db
from src.models import Funcionario, Produto

Funcionario = [
    {"id": 1, "name": "Jose Alcantra", "age": 34, "status": "Ativo"},
    {"id": 2, "name": "Mariana Gonçalves", "age": 28, "status": "Ativo"},
    {"id": 3, "name": "Augusto Pereira", "age": 29, "status": "Desativado"}
]






Produto = [
    {"id": 1, "nome_hotel": "Eco Pousada Beira Rio", "estrelas": 4, "valor_diaria": 350.0, "cidade": "Iporanga"},
    {"id": 2, "nome_hotel": "Porto Preguiças Resort", "estrelas": 5, "valor_diaria": 890.0, "cidade": "Barreirinhas"}
]

def seed():
    app = create_app()
    with app.app_context():
        if Funcionario.query.first():
            print("Banco já populado!")
            return

        print("Inserindo dados de Funcionarios...")
        for d in Funcionario:
            db.session.add(Funcionario(**d))
        
        for h in Produto:
            db.session.add(Produto(**h))
            
        db.session.commit()
        print("Seed finalizado com sucesso!")

if __name__ == '__main__':
    seed()