from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastApi is Running"}

@app.get("/health")
def health():
    return {"message":"OK"}

@app.get("/hello/{name}")
def say_hello(name:str):
    return {"Hello ":f"You are best {name}"}