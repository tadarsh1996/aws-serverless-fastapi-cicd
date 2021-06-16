from fastapi import FastAPI
from mangum import Mangum
import json
from api.v1.api import router as api_router


# from app.api.api_v1.api import router as api_router
# from mangum import Mangum

# app = FastAPI(title='Serverless Lambda FastAPI')

app = FastAPI()


@app.get("/",tags=["Endpoint Test"])
async def root():
    return {"message": "Hello World!"}

@app.get("/user")
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions Post!"}

  

app.include_router(api_router, prefix="/api/v1")
# handler = Mangum(app)



# @app.get("/",  tags=["Endpoint Test"])
# def main_endpoint_test():
#     return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}


# @app.get("/user",  tags=["Endpoint Test"])
# def main_endpoint_test():
#     return {"message": "Welcome CI/CD Pipeline with GitHub Actions Post!"}

# app.include_router(api_router, prefix="/api/v1")

# # handler = Mangum(app)

# # to make it work with Amazon Lambda, we create a handler object
# # handler = Mangum(app=app)
def handler(event, context):
    event['requestContext'] = {}  # Adds a dummy field; mangum will process this fine  
    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)
    return response

