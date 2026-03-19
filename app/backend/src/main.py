from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.controllers import car_controller
from src.repositories import database, entities
from fastapi.responses import JSONResponse

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car_controller.router)
