from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastApi is Walking and Running."}

@app.get("/health")
def health():
    return {"message":"OK"}

@app.get("/hello/{name}")
def say_hello(name:str):
    return {"Hello ":f"You are best {name}"}