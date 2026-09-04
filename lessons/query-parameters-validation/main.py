from typing import Annotated
from pydantic import AfterValidator
from fastapi import FastAPI, Query

app = FastAPI()


def check_coupon(coupon: str | None):
    if coupon is not None and not coupon.startswith("SAVE-"):
        raise ValueError("Your coupon should start with 'SAVE-'")
    return coupon


@app.get("/products")
def get_products(search: Annotated[str | None, Query(min_length=3, max_length=30)] = None,
                 *,
                 category: Annotated[str, Query(min_length=3, max_length=20)],
                 sort: Annotated[str | None, Query(pattern="^(name|price|rating)$")] = "name",
                 brand: Annotated[
                     str | None, Query(min_length=2, max_length=20, description="Tell us about the brand:")],
                 tags: Annotated[list[str] | None, Query()] = None,
                 limit: Annotated[int, Query(ge=1, le=50)] = 10,
                 product_name: Annotated[str, Query(alias="product-name")],
                 old_category: Annotated[
                     str | None, Query(deprecated=True, description="You should avoid using this.")],
                 debug: Annotated[str | None, Query(include_in_schema=False)] = None,
                 coupon: Annotated[str | None, AfterValidator(check_coupon)] = None):
    products_dict: dict = {}
    if search:
        products_dict.update({
            "search": search
        })
    if category:
        products_dict.update({
            "category": category
        })
    if sort:
        products_dict.update({
            "sort": sort
        })
    if brand:
        products_dict.update({
            "brand": brand
        })
    if tags:
        products_dict.update({
            "tags": tags
        })
    if limit:
        products_dict.update({
            "limit": limit
        })
    if product_name:
        products_dict.update({
            "product_name": product_name
        })
    if old_category:
        products_dict.update({
            "old_category": old_category
        })

    products_dict.update({
        "debug": debug
    })

    if coupon:
        products_dict.update({
            "coupon": coupon
        })

    return products_dict
