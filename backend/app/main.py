from fastapi import FastAPI
from app.db_config import Base


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World! changed not happend"}

