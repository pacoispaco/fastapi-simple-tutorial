# A simple tutorial to get started with FastAPI

## 1. Set up a Python project

1. Create project directory with templated `README.md`.
2. Create virtualenv:
```bash
$ virtualenv -p python3 env
```
3. Jump into the environment:
 ```bash
$ source env/bin/activate
```

To consider/discuss:
- [ ] What is a good README.md template for a Python API?
- [ ] Why create a Python virtual environment?
- [ ] Alternative ways to create a Python virtual environment?

## 2. Install FastAPI & uvicorn

FastAPI uses [uvicorn](https://www.uvicorn.org/) as a fast ASGI web server for Python that you can use for development purposes. It looks good enough for production too!

1. Browse https://fastapi.tiangolo.com/tutorial/
2. Create a `requirements.txt` file:
```
fastapi
uvicorn
```
3. Run:
```bash
(env) $ pip install -r requirements.txt
```

FastAPI also makes use of the Python  `typing` and `pydantic` modules. Both these modules are used to support the use of type declarations (via `typing`) and data validation and conversion (via `pedantic`) in FastAPI. This is cool and very useful!

4. The `typing` module was introduced into Python 3.5 as a standard module. Browse https://docs.python.org/3/library/typing.html.
5. The `pydantic` module is not a standard module, but is used by Fast API and installed when  FastAPI is installed. Browse https://pydantic-docs.helpmanual.io/.

## 3. Create a simple FastAPI program and run it

Use the Web Developer tools of your browser to inspect the responses of your API!

2. Create `main.py` (or whatever name you prefer):
```python
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def root ():
    return {"greeting": "Hello birds!", "number": 42}
```

> Note: The code for this step is in the [main3.py](./main3.py) file.

3. Run the FastAPI program with:
```bash
$ uvicorn main:api --reload
INFO:     Will watch for changes in these directories: ['...']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [182158] using watchgod
INFO:     Waiting for application startup.
INFO:     Application startup complete.
...
```

4. Point your favorite webbrowser to `http://127.0.0.1:8000`.

To consider/discuss:
- [ ] What is imported with fastapi?
- [ ] What is the fastapi.FastAPI object (api)?
- [ ] How does the @api decorator work?
- [ ] How is the function "root" and its name connected to the decorator?
- [ ] What are the arguments used to run the program with uvicorn, what do they mean and how do they relate to the program code?

5. Point your favorite webbrowser to `http://127.0.0.1:8000/docs`.

- [ ] What documentation does FastAPI generate? Try it out!
- [ ] What datatype are we returning from the function `root` and what datatype is the API returning to the browser?

## 4. Add a collections resource (and a simple database)

1. Add a function to  `main.py` for handling the path "/birds" and add a simple database in the form of a dictionary of birds:
```python
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
```

> Note: The code for this step is in the [main4.py](./main4.py) file.

2. Point your favorite web-browser to `http://127.0.0.1:8000/birds`.

 - [ ] Is the name of the FastAPI function that handles a specific path important? Why and in what way?
 - [ ] How is the resource URL pathname and the FastAPI function name related? What happens if they are different?
 - [ ] What datatype are we returning from the function `birds` and what datatype is the API returning to the browser?

## 5. Add a path parameter to a collections resource

1. Browse https://fastapi.tiangolo.com/tutorial/path-params/
2. Add a function to  `main.py` for handling the resource "/birds/{birdid}", but keep the function for handling "/birds":
```python
from fastapi import FastAPI

api = FastAPI()

db = {"birds": {"17852": "Trana",
                "25340": "Koltrast",
                "27361": "Blåmes",
                "27392": "Talgoxe"},
      "count": 4}

@api.get("/")
def root ():
    return {"greeting": "Hello birds!", "number": 42}

@api.get("/birds")
def birds ():
    return db

@api.get("/birds/{birdid}")
def bird (birdid):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        return "Bird with bird id %s not found." % (birdid)
```

> Note: The code for this step is in the [main5.py](./main5.py) file.

3. Point your favorite web-browser to `http://127.0.0.1:8000/birds/25340`.

To consider/discuss:
 - [ ] How is the resource URL pathname and the FastAPI function name related?
 - [ ] How is the resource path parameter name related to the function parameter name? What happens if they are different?

## 6. Add a type annotation to the parameter of a FastAPI function

1. Browse https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-with-types
2. Add a the type annotation `int` to the `birdid`  parameter of the function `bird`:
```python
@api.get("/birds/{birdid}")
def bird (birdid: int):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        return "Bird with bird id %s not found." % (birdid)
```

> Note: The code for this step is in the [main6.py](./main6.py) file.

3. Point your favorite web-browser to `http://127.0.0.1:8000/birds/25340`.

To consider/discuss:
 - [ ] What happened? And why? Note the type conversion of the path parameter!

 4. Change the keys in the "birds" dict in the simple database from strings to integers:
```python
db = {"birds": {17852: "Trana",
                25340: "Koltrast",
                27361: "Blåmes",
                27392: "Talgoxe"},
      "count": 4}
```

5. Point your favorite web-browser to `http://127.0.0.1:8000/birds/123abc`.

To consider/discuss:
 - [ ] What happened? and why?
 - [ ] What was the HTTP status code returned by the api?
 - [ ] Why is that HTTP status code returned? Read https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422

6. Point your favorite webbrowser to `http://127.0.0.1:8000/docs`.
 - [ ] What has happened in the documentation for the resource `/birds/{birdid}`?

## 7. Specify the HTTP status code to return

FastAPI provides the `status` module from [Starlette](https://www.starlette.io/).
1. Browse https://fastapi.tiangolo.com/advanced/response-change-status-code/ and https://github.com/encode/starlette/blob/master/starlette/status.py

### 7.1 Specify the default HTTP status code to return if all goes well

1. Import the FastAPI module `status` and set the default HTTP status code to return from a resource function, by adding that as a parameter to that function's decorator:
```python
from fastapi import FastAPI, status

...

@api.get("/birds/{birdid}", status_code = status.HTTP_200_OK)
def bird (birdid: int, response: Response):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        return "Bird with bird id %s not found." % (birdid)
```

> Note: The code for this step is in the [main7.py](./main7.py) file.

To consider/discuss:
 - [ ] What did the API return before we added the default status code?

### 7.2 Return the HTTP status code 404 Not found by setting the response status code

1. Add the proper HTTP status code for when an item in a collection resource is not found by returning the HTTP status code **404 Not found**.  Import the FastAPI modules `Response` and `status`:
```python
from fastapi import FastAPI, status, Response

...

@api.get("/birds/{birdid}", status_code = status.HTTP_200_OK)
def bird (birdid: int, response: Response):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
```

### 7.3 Return the HTTP status code 404 Not found by raising an exception and providing a message

1. Point your favorite web-browser to `http://127.0.0.1:8000/birds/9999`.

To consider/discuss:
 - [ ] What happened? and why?
 - [ ] What was the HTTP status code returned by the api?

3. Browse https://fastapi.tiangolo.com/tutorial/handling-errors/
4. Add the proper HTTP status code for when an item in a collection resource is not found by returning the HTTP status code **404 Not found**. Import the FastAPI module `HTTPException` and raise an HTTPException error.
```python
from fastapi import FastAPI, status, Response, HTTPException

...

@api.get("/birds/{birdid}")
def bird (birdid: int):
    if birdid in db["birds"]:
        return db["birds"][birdid]
    else:
        raise HTTPException(status_code=status.HTTP_NOT_FOUND, detail="Bird with birdid %d not found" % (birdid))
```

4. Point your favorite web-browser to `http://127.0.0.1:8000/birds/9999` and check the returned status code.

To consider/discuss:
 - [ ] When looking at the newtork traffic in the the Web Developer Tools window, what other resources are being accessed by the browser and what HTTP status codes are they returning. Should anything be done about them?

## 8. Add query parameters to a collection item resource

1. Browse https://fastapi.tiangolo.com/tutorial/query-params/
2. Add the query parameter `starts_with` to the function for handling the resource `/birds`:
 ```python
@api.get("/birds")
def birds (starts_with: str):
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
```

3. Point your favorite web-browser to `http://127.0.0.1:8000/birds`.

To consider/discuss:
 - [ ] Why do we get a status code of 422 Unprocessable Entity, and the message "field required"?

4. Browse https://fastapi.tiangolo.com/tutorial/query-params/#optional-parameters
5. Make the query parameter  `starts_with` in the collections resource "/birds" optional. Import the module `Optional` from the `typing` module, and modify the function "birds":
 ```python
from fastapi import FastAPI, HTTPException
from typing import Optional

...

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
```

6. Point your favorite web-browser to `http://127.0.0.1:8000/birds`.
7. Point your favorite web-browser to `http://127.0.0.1:8000/birds?starts_with=T`.

### 8.1 Handling misspelled and unsupported query parameters in a sane way

1. Point your favorite web-browser to `http://127.0.0.1:8000/birds?starts_wit=T`. Note the misspelling of `starts_wit`!

To consider/discuss:
 - [ ] What happens? Why?

2. Browse
   * https://github.com/tiangolo/fastapi/issues/1190
   * https://github.com/tiangolo/fastapi/pull/1297

To consider/discuss:
 - [ ] Should an API warn the client that they are using a non-recognized query parameter or not?
 - [ ] If so, is 404 Not Found a reasonable status code to return?

## 9. Documenting the API

FastAPI automatically generates documentation in the form of a live Open API spec that is in sync with the code. It is entirely based on Python docstrings and the use of the `typing` and `pydantic` modules.

1. Browse: https://fastapi.tiangolo.com/tutorial/first-steps/?h=#interactive-api-docs

### 9.1 Documenting a resource

1. Add a descriptive docstring to all functions handling resources:
```python
...

@api.get("/")
def root ():
    """The root resource which just returns a simple example **JSON object**."""

...

def birds (starts_with: Optional[str] = None)):
    """Return a collection of all the birds. If no query parameter is specified all birds are returned."""

...

def bird (birdid: int):
    """Return the bird with the given `birdid`."""
...
```

2. Point your favorite web-browser to `http://127.0.0.1:8000/docs` and look at the documentation for each resource.

To consider/discuss:
 - [ ] What kind of formatting can we use in the docstrings and how is the formatted text displayed in the Open API spec?

3. Add more extensive documentation with examples to a function handling a specific resource:
```python
def birds (starts_with: Optional[str] = None):
    """Return a collection of all the birds. If no query parameter is specified all birds are returned.

Examples:

* `/birds` will return all birds.
* `/birds?starts_with=T` will return all birds with a name beginning with a "T".
	"""
```

2. Point your favorite web-browser to `http://127.0.0.1:8000/docs` and look at the documentation for the above resource.

### 9.2 Documenting supported HTTP methods and returned HTTP status codes

TBD!

### 9.3 Documenting query and path parameters

1: Browse https://fastapi.tiangolo.com/tutorial/body-fields/#declare-model-attributes
2: Add documentation on the query parameter `starts_with` by first importing `Query` from `fastapi` and then using `Query` in the declaration of `starts_with` and provide a `description`:
```python
from fastapi import FastAPI, status, Response, Query

...

def birds (starts_with: Optional[str] = Query(None, description="Return birds whose names begin with the string `starts_with`.")):
    """Return a collection of all the birds. If no query parameter is specified all birds are returned.

...
```

1. Add documentation on the path parameter `{bird_id}` by first importing `Path`from `fastapi` and then using `Path` in the declaration of `bird_id` and provide a `description`. Note that you have to declare the `response` parameter before the `bird_id` parameter when you do this:
```python
from fastapi import FastAPI, status, Response, Query, Path

...

def bird (response: Response, birdid: int = Path (None, description="`birdid` is a five-digit number that identifies a specific bird.")):
    """Return the bird with the given `birdid`."""

... 
```

### 9.4 Adding general documentation on the API

1. Browse https://fastapi.tiangolo.com/tutorial/metadata/

2. Add som documentation of the entire API like this:
```python
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

...
```

To consider/discuss:
 - [ ] Point your favorite web-browser to `http://127.0.0.1:8000/docs` and look at the documentation for the API.
 - [ ] What kind of syntax can you use in the docstring?

## 10 Specifying default values for path and query parameters

## 11. Handling similar resource paths via function order

1. Read https://fastapi.tiangolo.com/tutorial/path-params/?h=#order-matters

## 12. HTTP Headers

### 12.1 Add HTTP headers to the response

### 12.2 Handling HTTP headers in the request

## 13. Using the power of async

Assume you want to paint your finger nails. There are two steps in doing this; painting the nail and then waiting for it to dry. Say it takes 1 minute to paint a nail and then 20 minutes for it to dry; in total that's 21 minutes for painting a single nail.

There are two strategies for painting all 10 finger nails:
1. You can paint your finger nails one finger nail at a time. First paint a nail, then wait for it to dry. Then paint the next nail, and wait for that to dry, etc. This will take 1+20 minutes * 10 = 210 minutes.
2. Or, you can paint your finger nails one finger nail at a time. First paint the first nail, then directly paint the next nail etc, without waiting for each nail to dry. This will take 10 * 1 minute + 20 minutes (for the last nail to dry) = 30 minutes.

Method 2 is done asynchronously. It's is obviously the better method if you want to finish faster. The general principle here is; if you have to wait for something, get on with the next thing you want to do in the meantime. This is exactly the idea behind async in Python (and similar features in other languages).

In Python (and other languages) you need to be specific about async in your code. You need to declare that a function can be asynchrounous, meaning if it has to wait for something, typically an IO-event to complete, it can yield program execution to a another function that is not waiting for anything.

The above situation occurs naturally in all API:s where you have multiple requests coming in to the API from different clients, with different functions in the API handling the reuquests. Why should one request have to wait for another request to complete if the other function is waiting on an IO-event, such as reading to or from a database?

1. Read https://fastapi.tiangolo.com/async/
2. Read https://stackabuse.com/python-async-await-tutorial/
3. Watch: https://youtu.be/iG6fr81xHKA
4. Watch: https://www.youtube.com/watch?v=tSLDcRkgTsY

## NN. Package the app as a Docker image

## NN. Run the Docker image as a container locally on your laptop

## NN. Run the Docker image as a container in Portainer
