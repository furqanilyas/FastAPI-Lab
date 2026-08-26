from fastapi import FastAPI, HTTPException
from lessons.models import Product

app = FastAPI()


@app.get("/")
def greet():
    return "Hello World"


product1 = Product(name="Laptop", id=1, description="Gaming laptop",
                   price=100, quantity=5)
product2 = Product(name="Mobile", id=2, description="Usage Mobiles",
                   price=50, quantity=10)
product3 = Product(name="Asus", id=3, description="Asus Work",
                   price=200, quantity=2)
product4 = Product(name="Machine", id=4, description="Washing Machine",
                   price=150, quantity=4)
product_list = [product1, product2, product3, product4]


@app.get("/products")
def products():
    return product_list

@app.get("/product/{id}")
def product_by_id(id: int):
    for item in product_list:
        if item.id == id:
            return item
    return "Product not found"

@app.get("/product/{id}/price")
def get_price(id: int):
    for item in product_list:
        if item.id == id:
            return {"id": item.id, "price": item.price}
    return "Product not found"

@app.post("/product")
def add_product(product: Product):
    for item in product_list:
        if product.id == item.id:
            raise HTTPException(status_code=409, detail="Product already exists")
    product_list.append(product)
    return product

@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for i in range(len(product_list)):
        if product_list[i].id == id:
            product.id = id
            product_list[i] = product
            return "Product updated successfully"
    return "Product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(product_list)):
        if product_list[i].id == id:
            del product_list[i]
            return "Product deleted successfully"
    return "Product not found"
