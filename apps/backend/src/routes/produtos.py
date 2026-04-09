from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Produto
from ..schemas.produto_schema import ProdutoSchema
from pydantic import ValidationError

produto_bp = Blueprint('Produtos', __name__, url_prefix='/Produtos')

@produto_bp.route('/', methods=['GET'])
def get_all():
    """
    Obtém todos os produtos
    ---
    tags:
      - Produto
    responses:
      200:
        description: Lista de produtos
        schema:
          id: 
            type: int
          description: 
            type: str
          price: 
            type: int
          estoque: 
            type: float
      404:
        description: Produto não encontrado
    """
   
    produtos = Produto.query.all()
    result = [ProdutoSchema(**p.to_dict()).model_dump() for p in produtos]
    return jsonify(result), 200


@produto_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um produto específico pelo ID
    ---
    tags:
      - Produto
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: OK
      404:
        description: Produto não encontrado
    """
    produto = Produto.query.get(id)

    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    
    return jsonify(produto.to_dict()), 200


@produto_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo produto
    ---
    tags:
      - Produtos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Produto'
    responses:
      201:
        description: Produto criado com sucesso
    """
    try:
       prod = ProdutoSchema(**request.json)
       novo_produto = Produto(**prod.model_dump())
       db.session.add(novo_produto)
       db.session.commit()
       
       return jsonify(novo_produto.to_dict()), 201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400
    
    
@produto_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um produto existente
    ---
    tags:
      - Produtos
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Produto'
    responses:
      200:
        description: OK
      404:
        description: Produto não encontrado
    """
    produto = Produto.query.get(id)

    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404

    try:
        prod_data = request.json
        produto.nome = prod_data.get('Nome', produto.nome)
        produto.description = prod_data.get('Descriçao', produto.description)
        produto.price = prod_data.get('Preço', produto.price)
        produto.estoque = prod_data.get('Estoque', produto.estoque)

        db.session.commit()
        return jsonify(produto.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@produto_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um produto
    ---
    tags:
      - Produto
    parameters:
      - in: path
        name: id
          type: integer
        description: 
            type: str
          price: 
            type: int
          estoque: 
            type: float
        description: ID do produto a ser removido
    responses:
      200:
        description: OK
      404:
        description: Produto não encontrado
    """  
    produto = Produto.query.get(id)

    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    
    db.session.delete(produto)
    db.session.commit()

    return jsonify({"mensagem": "Produto removido com sucesso"}), 200