from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

# Sample in-memory database
items = {}

# Item model
class Item(BaseModel):
    name: str
    description: Optional[str] = None

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items/")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.dict()
    return items[item_id]

