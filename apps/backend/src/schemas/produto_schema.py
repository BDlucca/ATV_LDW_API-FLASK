from pydantic import BaseModel

class ProdutoSchema(BaseModel):
    id: int
    name: str
    description: str
    price: int
    estoque: float