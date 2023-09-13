from fastapi import FastAPI

app = FastAPI()

# In-memory storage for items
items = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in items:
        return {"item_id": item_id, "item": items[item_id]}
    else:
        return {"message": "Item not found"}

@app.post("/items/")
def create_item(item: dict):
    item_id = len(items) + 1
    items[item_id] = item
    return {"item_id": item_id, "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if item_id in items:
        items[item_id] = item
        return {"item_id": item_id, "updated_item": item}
    else:
        return {"message": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted", "item_id": item_id}
    else:
        return {"message": "Item not found"}
