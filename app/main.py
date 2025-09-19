from fastapi import FastAPI

app = FastAPI(title="My FastAPI Project")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
