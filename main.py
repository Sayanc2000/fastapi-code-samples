from fastapi import FastAPI

from code_samples.SampleGenerator import SampleGenerator
from schemas import ItemCreate

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(data: ItemCreate):
    return {"item": data.dict()}


sample_object = SampleGenerator(app)

app.openapi_schema = sample_object.custom_openapi()
