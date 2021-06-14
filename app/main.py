from fastapi import FastAPI
from mangum import Mangum
import json
from api.v1.api import router as api_router

app = FastAPI(title='Serverless Lambda FastAPI')




@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}


@app.get("/",  tags=["Posts"])
def main_endpoint_test2():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions Post!"}

app.include_router(api_router, prefix="/api/v1")

handler = Mangum(app)

# to make it work with Amazon Lambda, we create a handler object
# handler = Mangum(app=app)
# def handler(event, context):
#     event['requestContext'] = {}  # Adds a dummy field; mangum will process this fine
    
#     asgi_handler = Mangum(app)
#     response = asgi_handler(event, context)
#     json_data = event["queryStringParameters"] 
#     # user = json_data["user"]
#     return {
#             "statusCode": 200,
#             "headers": {"Content-Type": "application/json"},
#             "body": json.dumps()
#             }

