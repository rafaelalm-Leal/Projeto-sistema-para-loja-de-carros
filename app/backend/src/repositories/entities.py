from sqlalchemy import Column, Integer, String, Float
from src.repositories.database import Base

class CarModel(Base):
    __tablename__ = "cars"

    placa = Column(String, primary_key=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    preco = Column(Float)
    foto = Column(String, nullable=True)
