from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    quantity: int
    description: str | None = None
    tax: float | None = None


@app.post("/products")
def add_product(product: Product):
    return {
        "message": "Product created",
        "product": product
    }


@app.put("/products/{product_id}")
def update_product(product_id: int, discount: int | float, product: Product):
    products_dict = product.model_dump()
    subtotal = product.price * product.quantity
    discount_amount = subtotal * discount / 100
    products_dict.update({
        "subtotal": subtotal,
        "discount_amount": discount_amount
    })
    if product.tax is not None:
        total = subtotal - discount_amount + product.tax
        products_dict.update({
            "total": total
        })
    else:
        total = subtotal - discount_amount
        products_dict.update({
            "total": total
        })

    return {
        "product_ID": product_id,
        **products_dict
    }
