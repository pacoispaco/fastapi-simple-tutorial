from fastapi import FastAPI, status, Response
from typing import Optional

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
def birds (starts_with: Optional[str] = None):
    if starts_with == None:
        return db
    else:
        hits = {"birds": {}}
        for key, item in db["birds"].items():
            if item.startswith(starts_with):
                hits["birds"][key] = item
        hits["count"] = len (hits["birds"])
        if hits["count"] == 0:
            response.status_code = status.HTTP_404_NOT_FOUND
        else:
            return hits

@api.get("/birds/{birdid}", status_code = status.HTTP_200_OK)
def bird (birdid: int, response: Response):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
