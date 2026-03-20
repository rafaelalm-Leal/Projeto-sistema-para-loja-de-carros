from sqlalchemy.orm import Session
from src.repositories.entities import CarModel

def list_cars(db: Session):
    return db.query(CarModel).all()

def create_car(db: Session, car_data):
    if get_car_internal(db, car_data.placa):
        raise ValueError(f"Carro com placa {car_data.placa} já existe")
    
    db_car = CarModel(**car_data.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_car_internal(db: Session, placa: str):
    return db.query(CarModel).filter(CarModel.placa == placa).first()

def search_car(db: Session, placa: str):
    car = get_car_internal(db, placa)
    if not car:
        raise ValueError(f"Carro com placa {placa} não encontrado")
    return car

def update_car(db: Session, placa: str, car_data: dict):
    db_car = search_car(db, placa)
    
    for key, value in car_data.items():
        setattr(db_car, key, value)
    
    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(db: Session, placa: str):
    db_car = search_car(db, placa)
    db.delete(db_car)
    db.commit()
    return True

def sell_car(db: Session, placa: str):
    db_car = search_car(db, placa)
    db_car.disponibilidade = False
    db.commit()
    db.refresh(db_car)
    return db_car