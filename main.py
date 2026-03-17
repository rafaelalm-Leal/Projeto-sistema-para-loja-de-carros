from fastapi import FastAPI
from schemas import car

app = FastAPI()

#Cadastro do carro
@app.get("/")
def home():
    return {"Mensagem": "Sistema funcionando"}

cars = []

@app.post("/cars")
def criar_carro(carro: car):
    cars.append(carro)
    return carro

#Buscar carro pela placa

@app.get("/cars/{placa}")
def buscar_carro(placa: str):
    placa_digitada = placa.upper()

    for carro in cars:
        if carro.placa.upper() == placa_digitada:
            return carro
    return {"erro: Carro não encontrado"}