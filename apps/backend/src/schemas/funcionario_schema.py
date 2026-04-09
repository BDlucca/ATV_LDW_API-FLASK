from pydantic import BaseModel

class FuncionarioSchema(BaseModel):
    id: int
    name: str
    age: int
    description: str
    active: bool = True