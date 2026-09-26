from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ProductBase(BaseModel):
    name: str
    price: float


class PhysicalProduct(ProductBase):
    weight: float


class DigitalProduct(ProductBase):
    file_size: float


@app.get("/products/{product_id}", response_model=PhysicalProduct | DigitalProduct)
def get_product_id():
    return PhysicalProduct(
        name="Laptop",
        price=200.20,
        weight=2.7
    )


@app.get("/products", response_model=list[PhysicalProduct | DigitalProduct])
def get_products():
    return []


@app.post("/product-prices", response_model=dict[str, float])
def get_product_prices(product: DigitalProduct):
    return {
        product.name: product.price
    }
