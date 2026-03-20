import pytest
from src.schemas.car_schema import CarResponse

def test_create_car(client):
    car_data = {
        "placa": "TST1234",
        "marca": "Toyota",
        "modelo": "Corolla",
        "ano": 2023,
        "preco": 150000.0,
        "disponibilidade": True
    }
    response = client.post("/cars/", json=car_data)
    assert response.status_code == 201
    assert response.json()["placa"] == "TST1234"

def test_list_cars(client):
    response = client.get("/cars/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_car(client):
    car_data = {
        "placa": "SEARCH1", "marca": "X", "modelo": "Y", "ano": 2020, "preco": 10.0
    }
    client.post("/cars/", json=car_data)
    
    response = client.get(f"/cars/{car_data['placa']}")
    assert response.status_code == 200
    assert response.json()["placa"] == car_data["placa"]

def test_search_car_not_found(client):
    response = client.get("/cars/NONEXISTENT")
    assert response.status_code == 404

def test_sell_car(client):
    car_data = {
        "placa": "SELL1", "marca": "X", "modelo": "Y", "ano": 2020, "preco": 10.0
    }
    client.post("/cars/", json=car_data)
    
    response = client.post(f"/cars/{car_data['placa']}/sell")
    assert response.status_code == 200
    assert response.json()["disponibilidade"] is False

def test_delete_car(client):
    car_data = {
        "placa": "DEL123", "marca": "X", "modelo": "Y", "ano": 2020, "preco": 10.0
    }
    client.post("/cars/", json=car_data)
    
    response = client.delete(f"/cars/{car_data['placa']}")
    assert response.status_code == 204
    
    # Verifica que sumiu
    search = client.get(f"/cars/{car_data['placa']}")
    assert search.status_code == 404
