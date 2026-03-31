from flask import Blueprint, jsonify

comand_bp = Blueprint('comanda', __name__)

COMAND_DB = [
    {
        "id": 1,
        "cliente": "Bruno de lucca",
        "numero": "10",
        "lanche": "sanduiches",
        "bebida": "bebida",
        "sobremesa": "sobremesa"
        "itens" : [
            { t}
        ]
    }
]

@comand_bp.route('/<int:id>', methods=['GET'])
def get_comand_details(id):
    """
    Obtém detalhes de uma bebida
    ---
    tags:
      - Bebidas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Detalhes da bebida
        schema:
          type: object
          properties:
            id:
              type: integer
            bebida:
              type: string
            tamanho:
              type: string
            gelado:
              type: boolen
      404:
        description: Bebida não encontrada
    """
    bebida = next((b for b in BEBIDA_DB if b['id'] == id), None)
    if bebida:
        return jsonify(bebida)
    return jsonify({"error": "Bebida not found"}), 404