# importing the FastAPI class from the fastapi module
from fastapi import FastAPI

# creating an instance of the FastAPI class
app = FastAPI()

# In-memory storage for items
items = {}

# defining the root endpoint of our API and returning a JSON (when a GET request is made to the root ["http://localhost:8000"] endpoint)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# defining a new endpoint that accepts a path parameter (item_id) and returns a JSON (when a GET request is made to the ["http://localhost:8000/items/{item_id}"] endpoint)
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # checking if the item_id exists in the items dictionary
    if item_id in items:
        return {"item_id": item_id, "item": items[item_id]}
    else:
        return {"message": "Item not found"}
    
# defining a new endpoint that accepts a path parameter (item_id) and returns a JSON (when a POST request is made to the ["http://localhost:8000/items/{item_id}"] endpoint)
@app.post("/items/")
def create_item(item: dict):
    # generating a new item_id by adding 1 to the length of the items dictionary
    item_id = len(items) + 1
    # adding the new item to the items dictionary
    items[item_id] = item
    return {"item_id": item_id, "item": item}

# defining a new endpoint that accepts a path parameter (item_id) and returns a JSON (when a PUT request is made to the ["http://localhost:8000/items/{item_id}"] endpoint)
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    # checking if the item_id exists in the items dictionary
    if item_id in items:
        # updating the item in the items dictionary
        items[item_id] = item
        return {"item_id": item_id, "updated_item": item}
    else:
        return {"message": "Item not found"}

# defining a new endpoint that accepts a path parameter (item_id) and returns a JSON (when a DELETE request is made to the ["http://localhost:8000/items/{item_id}"] endpoint)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # checking if the item_id exists in the items dictionary
    if item_id in items:
        # deleting the item from the items dictionary
        del items[item_id]
        return {"message": "Item deleted", "item_id": item_id}
    else:
        return {"message": "Item not found"}
