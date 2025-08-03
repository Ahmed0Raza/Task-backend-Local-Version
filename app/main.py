from fastapi import FastAPI
from config.database import engine

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}
