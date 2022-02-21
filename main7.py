from fastapi import FastAPI, status, Response

api = FastAPI()

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

@api.get("/birds/{birdid}", status_code = status.HTTP_200_OK)
def bird (birdid: int, response: Response):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
