from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Pedido
from ..schemas.pedido_schema import PedidoSchema
from pydantic import ValidationError

pedido_bp = Blueprint('Pedidos', __name__, url_prefix='/Pedidos')

@pedido_bp.route('/', methods=['GET'])
def get_all():
    """
    Obtém todos os pedidos
    ---
    tags:
      - Pedido
    responses:
      200:
        description: Lista de pedidos
        schema:
          id: 
          type: int
          number: 
          type: int
      404:
        description: Cliente não encontrada
    """
   
    pedidos = Pedido.query.all()
    result = [PedidoSchema(**p.to_dict()).model_dump() for p in pedidos]
    return jsonify(result), 200


@pedido_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um pedido específico pelo ID
    ---
    tags:
      - Pedido
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do pedido
    responses:
      200:
        description: OK
      404:
        description: Pedido não encontrado
    """
    pedido = Pedido.query.get(id)

    if not pedido:
        return jsonify({"error": "Pedido não encontrado"}), 404
    
    return jsonify(pedido.to_dict()), 200


@pedido_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo pedido
    ---
    tags:
      - Pedido
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Pedido'
    responses:
      201:
        description: Pedido criado com sucesso
    """
    try:
       ped = PedidoSchema(**request.json)
       novo_pedido = Pedido(**ped.model_dump())
       db.session.add(novo_pedido)
       db.session.commit()
       
       return jsonify(novo_pedido.to_dict()), 201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400
    
    
@pedido_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um pedido existente
    ---
    tags:
      - Pedido
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Pedido'
    responses:
      200:
        description: OK
      404:
        description: Pedido não encontrado
    """
    pedido = Pedido.query.get(id)

    if not pedido:
        return jsonify({"error": "Pedido não encontrado"}), 404

    try:
        ped_data = request.json
        pedido.number = ped_data.get('Numero', pedido.number)


        db.session.commit()
        return jsonify(pedido.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@pedido_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um pedido
    ---
    tags:
      - Pedido
    parameters:
      - in: path
        name: id
        type: integer
        number: int
        description: ID do pedido a ser removido
    responses:
      200:
        description: OK
      404:
        description: Pedido não encontrado
    """  
    pedido = Pedido.query.get(id)

    if not pedido:
        return jsonify({"error": "Pedido não encontrado"}), 404
    
    db.session.delete(pedido)
    db.session.commit()

    return jsonify({"mensagem": "Pedido removido com sucesso"}), 200