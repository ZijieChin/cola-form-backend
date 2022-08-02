from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

import uvicorn

from orm import connect_db, insert_db

app = FastAPI()


class Item(BaseModel):
    name: str
    options: Union[str, None] = None
    comment: Union[str, None] = None


@app.post("/api/v1/form")
async def root(item: Item):
    if insert_db(item):
        return {"result": 0}
    else:
        return {"result": 1}


if __name__ == "__main__":
    connect_db()
    uvicorn.run("main:app", port=5050, log_level="info")
