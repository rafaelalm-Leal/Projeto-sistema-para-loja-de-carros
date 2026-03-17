from pydantic import BaseModel

class car(BaseModel):
    placa: str
    marca: str
    modelo: str
    ano: int
    preco: float
    disponibilidade: bool