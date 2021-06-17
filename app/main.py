from fastapi import FastAPI
from mangum import Mangum
import json
from api.v1.api import router as api_router
from pydantic import BaseModel
from typing import List
import urllib.parse
import json
from pymongo import MongoClient
from typing import List


password="root123"
username="barkha"
client = MongoClient(
    "mongodb+srv://adarsh:Happy@new1-smr9o.mongodb.net/test?authSource=admin&replicaSet=new1-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
)
db = client.get_database('Database_fastapi')
# from app.api.api_v1.api import router as api_router
# from mangum import Mangum

# app = FastAPI(title='Serverless Lambda FastAPI')
DB = "Database_fastapi"
COLLECTION = "student"

app = FastAPI()


class Student(BaseModel):
    first_name: str
    last_name: str
    email: str
    mobile_number: int



@app.get("/",tags=["Endpoint Test"])
async def root():
    return {"message": "Hello World!"}

@app.get("/user")
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions Post!"}

  

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)

@app.post("/userput", status_code=status.HTTP_201_CREATED)
def post_message(user: Student):
        collection = db["student"] 
        print(collection)
        result = collection.insert_one(user.dict())
        print(result)
        return {"message":"Data inserted successfully"}

def handler(event, context):
    event['requestContext'] = {}  # Adds a dummy field; mangum will process this fine
    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)
    event["queryStringParameters"] 
    # user = json_data["user"]
    return response

