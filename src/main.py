from fastapi import FastAPI
from web import explorer
app = FastAPI()

app.include_router(explorer.router)
@app.get("/")
def top():
    return {"message": "Hello, World!"}

@app.get("/echo/{message}")
def echo(message: str):
    return {"message": message}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)