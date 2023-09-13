# FastAPI Tutorial - User Guide

## Installation

### Clone the repository

* Cloning the repository will create a local copy of the code on your machine.
* Clone the repository using the following command:

```bash 
git clone https://github.com/vaishnav-mk/fastapi-tutorial
```

### Change the working directory

* Change the working directory to the repository using the following command:

```bash
cd fastapi-tutorial
```

### Install the dependencies

* Install the fastapi dependencies using the following command:

```bash
pip install fastapi
```

## Usage

```bash
uvicorn main:app --reload
```

* `main` refers to the file `main.py`
* `app` refers to the variable `app` inside of `main.py`
* We can use the `--reload` flag to automatically reload the server when we make changes to the code.
* `uvicorn` is a server that runs our code and makes it accessible to the internet.

### Accessing the API

* The API is accessible at `http://localhost:8000`
* We can access the API using a web browser or a tool like **[Postman](https://www.postman.com/downloads)**.

### Swagger UI

* Swagger UI is a tool that automatically generates documentation for our API.
* It is accessible at `http://localhost:8000/docs`
* We can use Swagger UI to test our API.

## Creating a Basic API

### API Basics
#### What is an API?

* An API is an application programming interface.
* It is a set of functions and procedures that allow us to interact with an application.
* We can use an API to send and receive data from an application.

#### What is FastAPI?

* FastAPI is a Python framework for building APIs.
* It is a modern, fast, and easy to use framework.

#### What is Uvicorn?

* Uvicorn is a Python server that runs our code and makes it accessible to the internet.
* It is a fast, lightweight, and reliable server.

### Technical Overview

#### Types of Requests

* There are five main types of requests:
  * GET: Used to retrieve data from a server.
  * POST: Used to send data to a server.
  * PUT: Used to update data on a server.
  * DELETE: Used to delete data from a server.
  * PATCH: Used to update data on a server.
  
* We can use these requests to interact with our API.

#### What is a Route?

* A route is a path to a resource.
* We can use routes to access different parts of our API.

* Example: `http://localhost:8000/users` is a route that returns a list of users.
* There are two parts to this route:
  * The base URL: `http://localhost:8000`
  * The path: `/users`

#### What is a Path Parameter?

* A path parameter is a variable that is part of the path of a route.
* We can use path parameters to pass data to a route.

* Example: `http://localhost:8000/users/1` is a route that returns a user with the ID of 1.
* There are two parts to this route:
  * The base URL: `http://localhost:8000`
  * The path: `/users/1`
* The path parameter is `1`.

#### What is a Query Parameter?

* A query parameter is a variable that is part of the query string of a route.
* We can use query parameters to pass data to a route.

* Example: `http://localhost:8000/users?limit=10` is a route that returns a list of users with a limit of 10.
* There are two parts to this route:
  * The base URL: `http://localhost:8000`
  * The path: `/users`
* The query parameter is `limit=10`.

#### What is a Request Body?

* A request body is a variable that is part of the body of a request.
* We can use request bodies to pass data to a route.

* Example: `http://localhost:8000/users` is a route that creates a new user.
* There are two parts to this route:
  * The base URL: `http://localhost:8000`
  * The path: `/users`

  * The request body is a JSON object with the following properties:
    * `name`: The name of the user.
    * `age`: The age of the user.

Example:

```json
{
  "name": "John",
  "age": 30
}
```

#### What is a Response Body?

* A response body is a variable that is part of the body of a response.
* We can use response bodies to return data from a route.

* Example: `http://localhost:8000/users` is a route that returns a list of users.
* There are two parts to this route:
  * The base URL: `http://localhost:8000`
  * The path: `/users`

  * The response body is a JSON object with the following properties:
    * `name`: The name of the user.
    * `age`: The age of the user.

Example:
    
```json
[
    {
        "name": "John",
        "age": 30
    },
    {
        "name": "Jane",
        "age": 25
    }
]
```

#### What is a Status Code?

* A status code is a number that is part of the response.
* We can use status codes to indicate the status of a request.

* Example status codes:
    * `200`: OK
    * `201`: Created
    * `400`: Bad Request
    * `401`: Unauthorized
    * `403`: Forbidden
    * `404`: Not Found
    * `500`: Internal Server Error


#### What is JSON?

* JSON is a format for storing and exchanging data.
* It is a lightweight, human-readable, and language-independent data format.
* It is easy for humans to read and write.

* Example JSON object:

```json
{
  "name": "John",
  "age": 30
}
```


### Importing FastAPI

```python
from fastapi import FastAPI

app = FastAPI()
```

* We import the `FastAPI` class from the `fastapi` module.

### Creating a Route

```python
@app.get("/")
def index():
    return {"data": {"name": "John"}}
```

* We use the `app.get` decorator to create a route.
* The decorator takes a single argument, the path of the route.
* The function that the decorator is applied to is called when the route is accessed.
* The function must return a dictionary.
* The dictionary is converted to JSON and returned to the client.

### Creating a Route with `Parameters`

```python
@app.get("/users/{id}")
def get_user(id: int):
    return {"data": id}
```

* We can add parameters to the path of the route by enclosing them in curly braces.
* We can access the parameters in the function by adding an argument with the same name as the parameter.
* We can specify the type of the parameter by adding a colon and the type after the name of the parameter.
* We can also specify a default value for the parameter.

### Creating a Route with `Optional Parameters`

```python
@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

* We can make parameters optional by setting their default value to `None`.
* We can also specify the type of the parameter by adding a colon and the type after the name of the parameter.

### Creating a `POST` Route

```python
@app.post("/users")
def create_user(user: User):
    return {"data": f"User created with name {user.name}"}
```

* We can use the `app.post` decorator to create a POST route.
* The decorator takes a single argument, the path of the route.
* The function that the decorator is applied to is called when the route is accessed.
* The function must return a dictionary.

### Creating a `PUT` Route

```python
@app.put("/users/{id}")
def update_user(id: int, user: User):
    return {"data": f"User with id {id} has been updated with the following data: {user.dict()}"}
```

* We can use the `app.put` decorator to create a PUT route.
* The decorator takes a single argument, the path of the route.
* The function that the decorator is applied to is called when the route is accessed.
* The function must return a dictionary.

### Creating a `DELETE` Route

```python
@app.delete("/users/{id}")
def delete_user(id: int):
    return {"data": f"User with id {id} has been deleted"}
```

* We can use the `app.delete` decorator to create a DELETE route.
* The decorator takes a single argument, the path of the route.
* The function that the decorator is applied to is called when the route is accessed.
* The function must return a dictionary.

### Creating a `PATCH` Route

```python
@app.patch("/users/{id}")
def patch_user(id: int, user: User):
    return {"data": f"User with id {id} has been patched with the following data: {user.dict()}"}
```

* We can use the `app.patch` decorator to create a PATCH route.
* The decorator takes a single argument, the path of the route.
* The function that the decorator is applied to is called when the route is accessed.
* The function must return a dictionary.

## Using the example in the tutorial (`main.py`)
### Accessing the API

* The API is accessible at `http://localhost:8000`

### Swagger UI

* Swagger UI is accessible at `http://localhost:8000/docs`

### Routes

### `GET /` 

* When we access the route `http://localhost:8000/`, the function `read_root` is called.
* The function returns a dictionary with the following data:

```json
{
  "message": "Hello World"
}
```

### `GET /items/{item_id}`

* When we access the route `http://localhost:8000/items/{item_id}`, the function `read_item` is called.
* The function goes through the following steps:
  * Checks if the item exists in the database.
  * If the item exists, it returns a dictionary with the following data:

```json
{
  "item_id": item_id
}
```

  * If the item does not exist, it returns a dictionary with the following data:

```json
{
  "message": "Item not found"
}
```

### `POST /items/`

* When we access the route `http://localhost:8000/items/`, the function `create_item` is called.
* The function goes through the following steps:
  * Checks if the item exists in the database.
  * If the item exists, it returns a dictionary with the following data:

```json
{
  "message": "Item already exists"
}
```

  * If the item does not exist, it creates the item in the database and returns a dictionary with the following data:

```json
{
  "item_id": item_id,
  "item": item
}
```

### `PUT /items/{item_id}`

* When we access the route `http://localhost:8000/items/{item_id}`, the function `update_item` is called.
* The function goes through the following steps:
  * Checks if the item exists in the database.
  * If the item exists, it updates the item in the database and returns a dictionary with the following data:

```json
{
  "item_id": item_id,
  "item": item
}
```

  * If the item does not exist, it returns a dictionary with the following data:

```json
{
  "message": "Item not found"
}
```

### `DELETE /items/{item_id}`

* When we access the route `http://localhost:8000/items/{item_id}`, the function `delete_item` is called.
* The function goes through the following steps:
  * Checks if the item exists in the database.
  * If the item exists, it deletes the item from the database and returns a dictionary with the following data:

```json
{
  "message": "Item deleted",
  "item_id": item_id
}
```

  * If the item does not exist, it returns a dictionary with the following data:

```json
{
  "message": "Item not found"
}
```
