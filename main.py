from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000/helooworld
@app.get("/helooworld")
async def root():
    return{"message": "Hello World!"}

# 127.0.0.1:8000/funcaoteste
@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": "deu certo!"}