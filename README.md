# FastAPI tutorial

This project is a simple tuturial for getting started with writing web API:s with FastAPI. It grew out of my own studies and preparations for a workshop on FastAPI I held at work.

[Here is the tutorial](tutorial.md).

## Requirements

 * [FastAPI](https://fastapi.tiangolo.com/)
 * [uvicorn](https://www.uvicorn.org)

## Development

Set up the development environment with:

 1. Clone the git repo.
 2. Create a virtual env:
```
$ virtualenv -p python3 env
```
 3. Jump into the virtual env:
```
$ source env/bin/activate
```
 4. Install dependent packages with:
```
$ pip install -r requirements.txt
```
 5. Start hacking!

## Run

Provided the FastAPI app's main file is `main.py` and that the FastAPI application object is named **api**:
```
$ uvicorn main:api --reload
```
