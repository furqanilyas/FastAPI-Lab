from typing import Annotated

from fastapi import FastAPI, Cookie
from pydantic import BaseModel

app = FastAPI()


class UserCookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str
    theme: str | None = None
    language: str | None = None
    tracking_id: str | None = None


@app.get("/profile")
def get_cookie(
        cookie: Annotated[UserCookies, Cookie()]
):
    return {
        "cookies": cookie
    }
