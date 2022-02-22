from fastapi import FastAPI, status, Response, Path, Query
from typing import Optional

description="""
## A very simple Bird API.

This is a simple HTTP/JSON API implemented in Python & FastAPI that demonstrates some of the features in FastAPI. Among other things it demonstrates how to:
* Write a simple FastAPI application.
* Implement an API with a couple of resources.
* Implement support for different HTTP methods and return specific HTTP status codes.
* Use resource path parameters.
* Use resource query parameters.
* Write documentation for the auto-generated Open API Spec.
"""

api = FastAPI(
    title="The Birds API",
    description= description,
    version="0.0.1")

db = {"birds": {17852: "Trana",
                25340: "Koltrast",
                27361: "Blåmes",
                27392: "Talgoxe"},
      "count": 4}


@api.get("/")
def root ():
    """The root resource which just returns a simple example **JSON object**."""
    return {"greeting": "Hello birds!", "number": 42}

@api.get("/birds")
def birds (starts_with: Optional[str] = Query(None, description="Return birds whose names begin with the string `starts_with`.")):
    """Return a collection of all the birds. If no query parameter is specified all birds are returned.

Examples:

* `/birds` will return all birds.
* `/birds?starts_with=T` will return all birds with a name beginning with a "T".
	"""
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
def bird (response: Response, birdid: int = Path (None, description="`birdid` is a five-digit number that identifies a specific bird.")):
    """Return the bird with the given `birdid`."""
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
