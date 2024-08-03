from fastapi import FastAPI

app = FastAPI(
        title="Docker-App",
        version="0.1",
        description="This is a development work. testing out work."
        )

@app.get("/")
async def hello_world():
    return {"message":"Hello World!"}

@app.get("/user/{user_id}")
async def hello_user(user_id):
    return {"message":f"hello {user_id}"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
