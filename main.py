from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "FastApi is Walking and Running."}

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

@app.get("/hello/{name}")
def say_hello(name:str):
    return {"Hello ":f"You are best {name}"}