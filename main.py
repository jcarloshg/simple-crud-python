from typing import Union
from fastapi import FastAPI
# domain
from src.app.create_item.create_item import items
from src.app.create_item.create_item import create_item_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items")
async def get_all():
    return items

app.include_router(create_item_router)
