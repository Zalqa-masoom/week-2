import os
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
@app.get("/")
def read_root():
    app_title = os.getenv("APP_NAME", "Simple App")
    return {
        "message": "Hello from FastAPI!",
        "app_name": app_title
    }