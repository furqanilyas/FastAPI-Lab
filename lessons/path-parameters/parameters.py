from fastapi import FastAPI, Query
from enum import Enum

app = FastAPI()

products = [
    "Laptop",
    "Phone",
    "Tablet",
    "Keyboard",
    "Mouse"
]


class Category(str, Enum):
    laptop = "laptop"
    phone = "phone"
    tablet = "tablet"
    accessory = "accessory"


class SortOrder(str, Enum):
    newest = "newest"
    oldest = "oldest"
    price_low = "price_low"
    price_high = "price_high"


@app.get("/products")
def get_products(skip: int = Query(ge=0), limit: int = Query(le=5)):
    selected_products = products[skip: skip + limit]
    return {
        "products": selected_products
    }


@app.get("/products/{product_id}")
def get_product(product_id: int, category: Category | None = None, sort: SortOrder = SortOrder.newest,
                limit: int = Query(default=10, gt=1, lt=100), skip: int = 0, short: bool = False):
    product: dict = {
        "product_id": product_id
    }
    if category:
        product.update({
            "category": category
        })
    product.update({
        "sort": sort,
    })
    product.update({
        "limit": limit,
    })
    product.update({
        "skip": skip
    })
    if not short:
        product.update({
            "description": "This product has a detailed description."
        })

    return product
