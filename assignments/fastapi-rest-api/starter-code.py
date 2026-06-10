from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

_items: List[Item] = []

@app.get("/items", response_model=List[Item])
def list_items():
    return _items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    if any(i.id == item.id for i in _items):
        raise HTTPException(status_code=400, detail="ID already exists")
    _items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for i in _items:
        if i.id == item_id:
            return i
    raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
