from fastapi import FastAPI, Body
from uuid import UUID
from datetime import datetime, date, timedelta, time
from typing import Annotated
from decimal import Decimal

app = FastAPI()


@app.put("/files/{file_id}")
def update_file(file_id: UUID,
                *,
                filename: Annotated[str, Body()],
                created_at: Annotated[datetime, Body()],
                expires_on: Annotated[date, Body()],
                process_after: Annotated[timedelta, Body()],
                process_at: Annotated[time | None, Body()] = None,
                tags: Annotated[frozenset[str], Body()],
                content: Annotated[bytes, Body()],
                price: Annotated[Decimal, Body()]
                ):

    start_process = created_at + process_after

    days_expire = expires_on - created_at.date()

    return{
        "file_id": file_id,
        "filename": filename,
        "created_at": created_at,
        "expires_on": expires_on,
        "process_after": process_after,
        "process_at": process_at,
        "tags": tags,
        "price": price,
        "start_process": start_process,
        "days_expire": days_expire,
        "content": content
    }