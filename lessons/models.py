from pydantic import BaseModel

class Product(BaseModel):
    name: str
    id: int
    description: str
    price: float
    quantity: int

