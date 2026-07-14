from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Miora AI is running"
    }