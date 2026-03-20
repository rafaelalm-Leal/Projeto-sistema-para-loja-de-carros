from sqlalchemy.orm import Session
from src.repositories.entities import CarModel

def list_cars(db: Session, placa: str | None = None):
    query = db.query(CarModel)
    if placa:
        query = query.filter(CarModel.placa.contains(placa))
    return query.all()

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

def search_car(db: Session, placa: str) -> list[CarModel]:
    return db.query(CarModel).filter(CarModel.placa.contains(placa)).all()

def update_car(db: Session, placa: str, car_data: dict):
    db_car = get_car_internal(db, placa)
    
    for key, value in car_data.items():
        setattr(db_car, key, value)
    
    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(db: Session, placa: str):
    db_car = get_car_internal(db, placa)
    db.delete(db_car)
    db.commit()
    return True