from fastapi import FastAPI
from pymongo import MongoClient
from people_routes import router as people_router

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("localhost", 27017)
    app.database = app.mongodb_client["testing"]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(people_router, tags=["people"], prefix="/people")
