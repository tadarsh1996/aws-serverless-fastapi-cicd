
from fastapi import FastAPI, status
from mangum import Mangum
from pymongo import MongoClient
# from pydantic import BaseModel
from typing import List
import urllib.parse
import json
from api.v1.api import router as api_router
# password="root123"
# username="barkha"
# client = MongoClient(
#     "mongodb+srv://"+urllib.parse.quote_plus(username)+":"+urllib.parse.quote_plus(password)+"@cluster0.otmoo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
# )
# db = client.get_database('myFirstDatabase')


app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

DB = "myFirstDatabase"
COLLECTION = "users"

# Message class defined in Pydantic
# class User(BaseModel):
#     first_name: str
#     last_name: str
#     email: str
#     mobile_number: int

@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}

def handler(event, context):
    event['requestContext'] = {}  # Adds a dummy field; mangum will process this fine  
    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)
    return response

# adding user
# @app.post("/user", status_code=status.HTTP_201_CREATED)
# def post_message(user: User):
#         collection = db["users"] 
#         print(collection)
#         result = collection.insert_one(user.dict())
#         print(result)
#         return {"message":"Data inserted successfully"}

# getting all users
# @app.get("/user", response_model=List[User])
# def get_users():
#         collection = db["users"] 
#         user_list = collection.find()
#         users=[]
#         for i in user_list:
#             users.append(User(**i))
#         print(users)
#         return users

# # getting single user by id
# @app.get("/user/{user_id}", response_model=List[User])
# def get_users():
#         collection = db["users"] 
#         user = collection.find()
#         users=[]
#         for i in user_list:
#             users.append(User(**i))
#         print(users)
#         return users



# from fastapi import FastAPI
# from mangum import Mangum
# import json
# from api.v1.api import router as api_router


# # from app.api.api_v1.api import router as api_router
# # from mangum import Mangum

# app = FastAPI(title='Serverless Lambda FastAPI')

# app = FastAPI()
# app.include_router(api_router, prefix="/api/v1")

# @app.get("/",  tags=["Endpoint Test"])
# def main_endpoint_test():
#     return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}

# @app.get("/user")
# def main_endpoint_test():
#     return {"message": "Welcome CI/CD Pipeline with GitHub Actions Post!"}

  
# def handler(event, context):
#     event['requestContext'] = {}  # Adds a dummy field; mangum will process this fine  
#     asgi_handler = Mangum(app)
#     response = asgi_handler(event, context)
#     return response

