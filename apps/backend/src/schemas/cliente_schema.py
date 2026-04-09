from pydantic import BaseModel

class ClienteSchema(BaseModel):
    id: int
    name: str
    age: int
    total_pagar: float