from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI on Vercel working!"}

handler = Mangum(app)  # This is important for serverless