from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Cliente
from ..schemas.cliente_schema import ClienteSchema
from pydantic import ValidationError

cliente_bp = Blueprint('Clientes', __name__, url_prefix='/Clientes')

@cliente_bp.route('/<int:id>', methods=['GET'])
def get_all():
    """
    Obtém detalhes de um Cliente
    ---
    tags:
      - Cliente
    parameters:
      - id: int
      - name: str
    responses:
      200:
        description: Detalhes do clientes
        schema:
          id: 
          type: int
          name: 
          type: str
          age: 
          type: int
          total_pagar: 
          type: int
      404:
        description: Cliente não encontrada
    """
   
    clientes = Cliente.query.all()
    result = [ClienteSchema(**c.to_dict()).model_dump() for c in clientes]
    return jsonify(result), 200

@cliente_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um clinte específico pelo ID
    ---
    tags:
      - Cliente
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do registro
    responses:
      200:
        description: OK
    """
    cliente1 = Cliente.query.get(id)

    if not cliente1:
        return jsonify({"error": "Cliente não encontrada"}), 404
    
    return jsonify(cliente1.to_dict()), 200

    
@cliente_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo cliente
    ---
    tags:
      - Cliente
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Cliente'
    responses:
      200:
        description: Cliente criada com sucesso
        schema:
          $ref: '#/definitions/Cliente'
    """
    try:
       cli = ClienteSchema(**request.json)
       novo_cliente = Cliente(**cli.model_dump())
       db.session.add(novo_cliente)
       db.session.commit()
       
       return jsonify(novo_cliente.to_dict()),201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400
    
    
@cliente_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um cliente existente
    ---
    tags:
      - Cliente
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Cliente'
    responses:
      200:
        description: OK
    """
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify ({"error": "Reserva não encontrada"}), 404
    try:
        cli1 = request.json
        cliente.nome = cli1.get('Nome', cliente.nome)
        cliente.age = cli1.get('Idade', cliente.age)
        cliente.total_pagar = cli1.get('Total_pagar', cliente.total_pagar)

        db.session.commit()
        return jsonify(cliente.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@cliente_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um cliente
    ---
    tags:
      - Cliente
    parameters:
      - in: path
        name: id
        type: integer
        age: int
        description: ID do registro a ser removido
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """  
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    
    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"mensagem":"Cliente removido com sucesso"}), 200