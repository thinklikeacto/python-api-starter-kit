from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

app = FastAPI()

# MongoDB setup
MONGO_DETAILS = os.getenv("MONGO_DETAILS")  # MongoDB connection string
print("MONGO_DETAILS is: ", MONGO_DETAILS)
mongo_client = MongoClient(MONGO_DETAILS)

@app.on_event("startup")
async def startup_event():
    global kafka_producer
    # Connect to MongoDB
    try:
        mongo_client.server_info()  # Force a call to check the connection
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        raise HTTPException(status_code=500, detail=f"MongoDB connection failed: {e}")
    
@app.get("/")
async def root():
    return {"message": "Hello World"}