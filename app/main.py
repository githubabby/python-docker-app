import logging
logger = logging.getLogger('SimpleLog')
logging.basicConfig(
    filename='simple.log',
    encoding='utf-8',
    format='%(asctime)s :%(name)s:%(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    level=logging.DEBUG
)


from fastapi import FastAPI

app = FastAPI(
        title="Docker-App",
        version="0.1",
        description="This is a development work. testing out work."
        )

@app.get("/")
async def hello_world():
    logger.info("hello world is called!")
    return {"message":"Hello World!"}

@app.get("/user/{user_id}")
async def hello_user(user_id):
    logger.info(f"hello world with {user_id=} is called!")
    return {"message":f"hello {user_id}"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
