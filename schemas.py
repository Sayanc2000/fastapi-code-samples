from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    price: float
    is_offer: bool = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Item1",
                "price": 100,
                "is_offer": True,
            }
        }
