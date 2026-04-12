from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Funcionario
from ..schemas.funcionario_schema import FuncionarioSchema
from pydantic import ValidationError

funcionario_bp = Blueprint('Funcionarios', __name__, url_prefix='/Funcionarios')

@funcionario_bp.route('/<int:id>', methods=['GET'])
def get_all():
    """
    Obtém detalhes de um Funcionario
    ---
    tags:
      - Funcionario
    parameters:
      - id: int
      - name: str
    responses:
      200:
        description: Detalhes do funcionario
        schema:
          id: 
          type: int
          name: 
          type: str
          age: 
          type: int
          description:
          active: True
      404:
        description: Funcionario não encontrado
    """
   
    funcionarios = Funcionario.query.all()
    result = [FuncionarioSchema(**f.to_dict()).model_dump() for f in funcionarios]
    return jsonify(result), 200


@funcionario_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um funcionario específico pelo ID
    ---
    tags:
      - Funcionario
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
    funcionario = Funcionario.query.get(id)

    if not funcionario:
        return jsonify({"error": "Funcionario não encontrado"}), 404
    
    return jsonify(funcionario.to_dict()), 200


@funcionario_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo funcionario
    ---
    tags:
      - Funcionario
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Funcionario'
    responses:
      200:
        description: Funcionario criado com sucesso
        schema:
          $ref: '#/definitions/Funcionario'
    """
    try:
       func = FuncionarioSchema(**request.json)
       novo_funcionario = Funcionario(**func.model_dump())
       db.session.add(novo_funcionario)
       db.session.commit()
       
       return jsonify(novo_funcionario.to_dict()), 201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400
    
    
@funcionario_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um funcionario existente
    ---
    tags:
      - Funcionario
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Funcionario'
    responses:
      200:
        description: OK
    """
    funcionario = Funcionario.query.get(id)

    if not funcionario:
        return jsonify({"error": "Funcionario não encontrado"}), 404

    try:
        func_data = request.json
        funcionario.nome = func_data.get('Nome', funcionario.nome)
        funcionario.age = func_data.get('Idade', funcionario.age)
        funcionario.active = func_data.get('Status', funcionario.active)

        db.session.commit()
        return jsonify(funcionario.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@funcionario_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um funcionario
    ---
    tags:
      - Funcionario
    parameters:
      - in: path
        name: id
        type: integer
        description: ID do registro a ser removido
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """  
    funcionario = Funcionario.query.get(id)

    if not funcionario:
        return jsonify({"error": "Funcionario não encontrado"}), 404
    
    db.session.delete(funcionario)
    db.session.commit()

    return jsonify({"mensagem": "Funcionario removido com sucesso"}), 200