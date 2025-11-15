from fastapi import FastAPI
# domain
from src.app.create_item.create_item import create_item_router
from src.app.get_all.get_all import get_all_items_router

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello, this is the main endpoint of the API"


app.include_router(get_all_items_router)
app.include_router(create_item_router)
