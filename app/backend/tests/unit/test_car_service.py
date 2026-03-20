import pytest
from src.services import car_service
from src.schemas.car_schema import CarCreate

def test_service_create_car(db_session):
    car_data = CarCreate(
        placa="SERV1", marca="S", modelo="X", ano=2021, preco=100.0
    )
    result = car_service.create_car(db_session, car_data)
    assert result.placa == "SERV1"
    assert result.marca == "S"

def test_service_create_duplicate_placa(db_session):
    car_data = CarCreate(
        placa="DUP1", marca="D", modelo="X", ano=2021, preco=100.0
    )
    car_service.create_car(db_session, car_data)
    
    with pytest.raises(ValueError) as exc:
        car_service.create_car(db_session, car_data)
    
    assert "já existe" in str(exc.value)

def test_service_search_car(db_session):
    car_data = CarCreate(
        placa="SRCH1", marca="S", modelo="X", ano=2021, preco=100.0
    )
    car_service.create_car(db_session, car_data)
    
    result = car_service.search_car(db_session, "SRCH1")
    assert result.placa == "SRCH1"

def test_service_search_not_found(db_session):
    with pytest.raises(ValueError) as exc:
        car_service.search_car(db_session, "NONEXISTENT")
    assert "não encontrado" in str(exc.value)

def test_service_sell_car(db_session):
    car_data = CarCreate(
        placa="SELL_SRV", marca="S", modelo="X", ano=2021, preco=100.0, disponibilidade=True
    )
    car_service.create_car(db_session, car_data)
    
    result = car_service.sell_car(db_session, "SELL_SRV")
    assert result.disponibilidade is False
