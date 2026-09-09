from typing import Annotated
from pydantic import BaseModel, HttpUrl, Field

from fastapi import FastAPI, Query, Body

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Manufacturer(BaseModel):
    name: str
    country: str


class Product(BaseModel):
    name: str = Field(min_length=3)
    description: str | None = None
    price: float = Field(gt=0)
    tax: float | None = None
    tags: set[str]
    images: list[Image] | None = None
    manufacturer: Manufacturer


@app.post("/products/{product_id}")
def create_product(product_id: int,
                   notify: Annotated[bool, Query()] = False,
                   *,
                   product: Product,
                   importance: Annotated[int, Body(ge=1, le=10)]):
    return {
        "product_id": product_id,
        "product": product,
        "importance": importance,
        "notify": notify
    }
