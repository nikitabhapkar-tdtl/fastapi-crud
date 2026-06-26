from fastapi import FastAPI
from app.database import Base, engine
from app import models 
from app.routers import employee

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employee.router)