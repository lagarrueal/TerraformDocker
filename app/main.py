from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/night")
async def root():
    return {"message" : "Good Night"}

@app.get("/add/{a}/{b}")
async def read_item(a: int, b : int):
    return {"result" : a + b}

@app.get("/multiply/{a}/{b}")
async def read_item(a: int, b : int):
    return {"result" : a * b}