from typing import Annotated 
import logging
import json
from mylogger import CONFIG
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
import uvicorn.logging as ulog

logging.config.dictConfig(json.loads(CONFIG))

app = FastAPI(
        title="Docker-App",
        version="0.1",
        description="This is a development work. testing out work."
        )

@app.get("/")
async def hello_world():
    ulog.logging.info("calling info from ulog")
    logging.info("hello world is called!")
    return {"message":"Hello World!"}

@app.get("/user/{user_id}")
async def hello_user(user_id: Annotated[int, 'user_id to get']):
    logging.info(f"hello world with {user_id=} is called!")
    return {"message":f"hello {user_id}"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logging.warning(f"OMG! The client sent invalid data!: {exc}")
    return PlainTextResponse("There is a validation error", status_code=400)


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
