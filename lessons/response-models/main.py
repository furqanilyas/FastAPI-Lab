from fastapi import FastAPI, HTTPException
from models import UserOut, UserIn, BaseProduct, ProductIn, Item
from data import products

app = FastAPI()


@app.post("/signup", response_model=UserOut)
def sign_up(user: UserIn):
    return user


@app.post("/products")
def create_product(product: ProductIn) -> BaseProduct:
    return product


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def get_item(item_id: int):
    for item in products:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Product with this IS doesn't exist.")


@app.get("/products/{product_id}", response_model=Item, response_model_exclude={"tax"})
def get_product(product_id: int):
    for item in products:
        if item.id == product_id:
            return item
    raise HTTPException(status_code=404, detail="Product with this IS doesn't exist.")
