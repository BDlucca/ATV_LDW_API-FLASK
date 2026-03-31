from flask import Blueprint, jsonify

bebida_bp = Blueprint('bebida', __name__)

BEBIDA_DB = [
    {
        "id": 1,
        "bebida": "Café com leite",
        "tamanho":"pequeno",
        "gelado":"true"
    },
    {
        "id":2,
        "bebida":"capuccino",
        "tamanho": "medio",
        "gelado": "False"
    },
    {
        "id": 3,
        "bebida": "Chá",
        "tamanho": "pequeno",
        "gelado": "False"
    }
]

@bebida_bp.route('/<int:id>', methods=['GET'])
def get_bebida_details(id):
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