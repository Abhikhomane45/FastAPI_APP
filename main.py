from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.model import TaskModel

Base.metadata.create_all(engine)

app=FastAPI()

@app.get("/")
def home():
    return "This is Task Management App using FastAPI "