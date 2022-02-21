from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def root ():
    return {"greeting": "Hello birds!", "number": 42}
