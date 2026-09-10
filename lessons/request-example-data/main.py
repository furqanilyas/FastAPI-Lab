from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    description: str
    category: str
    in_stock: bool

@app.post("/products")
def create_product(product: Annotated[Product, Body(
    openapi_examples={
        "Best Seller":{
            "summary": "This example is for the best seller.",
            "description": "Top-notch option for best seller.",
            "value": {
                "name": "Gaming Laptop",
                "price": 145000,
                "description": "High-performance gaming laptop",
                "category": "electronics",
                "is_stock": True
            }
        },

        "Budget":{
            "summary": "This example is for the budget.",
            "description": "Top-notch option for low-budget.",
            "value": {
                "name": "Wireless Mouse",
                "price": 2500,
                "description": "Affordable wireless mouse",
                "category": "accessories",
                "is_stock": True

            }
        },

        "Out of Stock": {
            "summary": "This example is for the Out of Stock.",
            "description": "Out of Stock Stuff.",
            "value": {
                "name": "Mechanical Keyboard",
                "price": 12000,
                "description": "RGB mechanical keyboard",
                "category": "accessories",
                "is_stock": False

            }
        }
    }
)]):

    return product