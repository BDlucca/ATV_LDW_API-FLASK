from pydantic import BaseModel

class PedidoSchema(BaseModel):
    id: int
    number: int