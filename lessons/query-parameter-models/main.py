from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Literal, Annotated

app = FastAPI()

class ProductFilter(BaseModel):

    model_config = {"extra": "forbid"}
    limit: int = Field(20, gt=0, le=100)
    offset: int = Field(0, ge=0)
    sort: Literal["price","name","rating"] = "price"
    search: str | None = None
    category: str | None = None
    tags: list[str] = []

@app.get("/products")
def get_products(filters: Annotated[ProductFilter, Query()]):
    return filters