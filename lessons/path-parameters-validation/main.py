from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/products/{product_id}")
def get_product(product_id: Annotated[int, Path(ge=1, title="Enter product ID to get product.")],
                price: Annotated[float, Query(gt=0)],
                quantity: Annotated[int, Query(gt=1, lt=100)],
                discount: Annotated[float | None, Query(ge=0, lt=100)] = None):
    products_dict = {}

    products_dict.update({
        "product_id": product_id
    })
    products_dict.update({
        "price": price
    })
    products_dict.update({
        "quantity": quantity
    })
    products_dict.update({
        "discount": discount
    })

    return products_dict
