from fastapi import FastAPI

api = FastAPI()

db = {"birds": {"17852": "Trana",
                "25340": "Koltrast",
                "27361": "Blåmes",
                "27392": "Talgoxe"},
      "count": 4}

@api.get("/")
def root ():
    return {"greeting": "Hello world!", "number": 42}

@api.get("/birds")
def birds ():
    return db
