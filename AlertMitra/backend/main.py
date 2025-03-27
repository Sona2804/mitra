from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Disaster Alert System API is Running"}