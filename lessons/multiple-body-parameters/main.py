from typing import Annotated

from pydantic import BaseModel
from fastapi import FastAPI, Body

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

class Customer(BaseModel):
    username: str
    email: str

@app.post("/orders/{order_id}")
def create_order_product(order_id: int, product: Product, customer: Customer, quantity: Annotated[int, Body()]):
    return {
        "order_id": order_id,
        "product": product,
        "customer": customer,
        "quantity": quantity
    }

@app.post("/orders")
def create_product(product: Annotated[Product, Body(embed=True)]):
    return {
        "product": product
    }
