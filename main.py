from fastapi import FastAPI

from fastapi_code_samples.CustomAuth import CustomAuth
from fastapi_code_samples.SampleGenerator import SampleGenerator
from schemas import ItemCreate

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(data: ItemCreate):
    return {"item": data.dict()}


auth_config = CustomAuth(
    header='Authorization',
    prefix='Bearer',
    sample_token='1234'
)
sample_object = SampleGenerator(app, auth_config=auth_config)

app.openapi_schema = sample_object.custom_openapi()
