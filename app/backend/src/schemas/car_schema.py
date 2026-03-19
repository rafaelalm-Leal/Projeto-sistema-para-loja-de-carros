from pydantic import BaseModel, ConfigDict
from typing import Optional

class CarBase(BaseModel):
    placa: str
    marca: str
    modelo: str
    ano: int
    preco: float
    disponibilidade: bool = True
    foto: Optional[str] = None

class CarCreate(CarBase):
    pass

class CarUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano: Optional[int] = None
    preco: Optional[float] = None
    disponibilidade: Optional[bool] = None
    foto: Optional[str] = None

class CarResponse(CarBase):
    model_config = ConfigDict(from_attributes=True)