from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List

from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from orm import connect_db, insert_db, query_db

origins = [
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Choice(BaseModel):
    value: str
    chosen: int
    note: Union[str, None] = None

class Item(BaseModel):
    factory: str
    choices: List[Choice]


@app.post("/api/v1/form")
async def root(item: Item):
    if insert_db(item):
        return {"result": 0}
    else:
        return {"result": 1}

@app.get("/api/v1/query")
async def query():
    query_db()
    return {"result": 0}


if __name__ == "__main__":
    connect_db()
    uvicorn.run("main:app", port=5050, log_level="info")
