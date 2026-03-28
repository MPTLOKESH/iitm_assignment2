from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI(
    title="Assignment 2",
    description="",
    version="1.0.0"
)

items = [
    {"id":1, "name": "shirt", "price": 999},
    {"id":2, "name": "pant", "price": 799}
]

@app.get("/")
def root():
    return {"message": "Hello world"}

@app.get("/data", response_model=List[dict])
def get_all_item():
    return items

@app.get("/data/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
        raise HTTPException(status_code=404, detail="Item not found")

@app.post("/data")
def add_item(item: dict):
    items.append(item)
    return{
        "message": "Item added successfully",
        "item" : item
    }