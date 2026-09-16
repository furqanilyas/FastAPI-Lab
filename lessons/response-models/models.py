from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class BaseProduct(BaseModel):
    name: str
    price: float
    description: str | None = None


class ProductIn(BaseProduct):
    internal_sku: str


class Item(BaseModel):
    id: int
    price: float
    tax: float = 10.5
