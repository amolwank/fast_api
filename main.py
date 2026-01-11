from fastapi import FastAPI, Response
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, generate_latest

app = FastAPI()
Instrumentator().instrument(app).expose(app)
REQUESTS = Counter("http_requests_total", "Total HTTP Requests")

@app.get("/")
def home():
    return {"message": "FastApi is Walking and Running and Fucking."}

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

@app.get("/hello/{name}")
def say_hello(name:str):
    return {"Hello ":f"You are best {name}"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")