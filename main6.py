from fastapi import FastAPI

api = FastAPI()

#db = {"birds": {"17852": "Trana",
#                "25340": "Koltrast",
#                "27361": "Blåmes",
#                "27392": "Talgoxe"},
#      "count": 4}
db = {"birds": {17852: "Trana",
                25340: "Koltrast",
                27361: "Blåmes",
                27392: "Talgoxe"},
      "count": 4}


@api.get("/")
def root ():
    return {"greeting": "Hello birds!", "number": 42}

@api.get("/birds")
def birds ():
    return db

@api.get("/birds/{birdid}")
def bird (birdid: int):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        return "Bird with bird id %s not found." % (birdid)
