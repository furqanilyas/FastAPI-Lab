from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class RequestHeaders(BaseModel):
    model_config = {"extra":"forbid"}
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str]


@app.get("/products")
def get_product(header: Annotated[RequestHeaders, Header()]):
    return {
        "header": header
    }