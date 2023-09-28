# Item Management System

from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI(
    title="FastAPI Testing Project",
    description="Simple item managment API",
    version="0.0.0"
)

class Category(Enum):
    """Category of an item"""
    TOOLS = "tools"
    CONSUMABLES = "consumables"

class Item(BaseModel):
    """Represemtation of an item object"""
    name: str = Field(description="Name of the item.")
    price: float = Field(description="Price of the item in USD.")
    count: int = Field(description="Amount of instances of this item available in stock.")
    id: int = Field(description="Unique id for item.")
    category: Category = Field(description="Category of this item.")

# Example items data
items = {
    0: Item(name="Screwdriver", price=10.5, count=3, id=0, category=Category.TOOLS),
    1: Item(name="Wrench", price=20.0, count=1, id=1, category=Category.TOOLS),
    2: Item(name="Drill", price=50.0, count=2, id=2, category=Category.TOOLS),
    3: Item(name="Nails", price=5.0, count=100, id=3, category=Category.CONSUMABLES),
    4: Item(name="Screws", price=5.0, count=100, id=4, category=Category.CONSUMABLES),
}

# Get all items and values
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

# Get item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail=f"Item with {item_id=} does not found.",
        )
    return items[item_id]

# Get query item by parameters
@app.get("/items")
def get_query_item(
    name: str = None,
    price: float = None, 
    count: int = None, 
    id: int = None, 
    category: Category = None
    ) -> Item:
    
    for item in items.values():
        if item.name == name or item.price == price or item.count == count or item.id == id or item.category == category:
            return item
    raise HTTPException(
        status_code=404,
        detail=f"Item with {name=} or {price=} or {count=} or {id=} or {category=} does not found.",
    )
    
# Add item using post request
@app.post("/")
def add_item(item: Item) -> dict[int, Item]:
    if item.id in items:
        raise HTTPException(
            status_code=400,
            detail=f"Item with {item.id=} already exists.",
        )
    items[item.id] = item
    return {item.id: item}

# Update items by item id
@app.put(
    "/update/{item_id}",
    responses={
        404: {"description": "Item not found."},
        400: {"description": "Item id mismatch. No arguments specified."},
    }
)

def update_item(
    item_id: int,
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None
) -> Dict[int, Item]:  # Updated response type to match the returned value
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail=f"Item with {item_id=} does not found.",
        )
    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count
    if category is not None:
        item.category = category
    return {item_id: item}  # Return a dictionary with integer keys

# Item delete
@app.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail=f"Item with {item_id=} does not found.",
        )
    del items[item_id]
    return {"message": "Item deleted successfully."}    