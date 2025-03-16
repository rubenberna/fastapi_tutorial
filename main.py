from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    """
    Enumeration for model names.
    """
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    """
    Root endpoint that returns a simple JSON message.
    """
    return {"message": "Hello World"}


@app.get("/users/me")
async def get_curret_user():
    """
    Endpoint to get the current user.

    Returns:
        dict: A dictionary containing the user ID of the current user.
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """
    Endpoint to get a user by their ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict: A dictionary containing the user ID.
    """
    return {"user_id": user_id}


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    """
    Endpoint to get a model by its name.

    Args:
        model_name (ModelName): The name of the model.

    Returns:
        dict: A dictionary containing the model name and a message.
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name == ModelName.lenet:
        return {"model_name": model_name, "message": "LeNet all the things!"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    Endpoint to read a file by its path.

    Args:
        file_path (str): The path of the file.

    Returns:
        dict: A dictionary containing the file path.
    """
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    Endpoint to read items with optional query parameters.
    When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

    Args:
        skip (int): The number of items to skip.
        limit (int): The number of items to limit the response to.

    Returns:
        dict: A dictionary containing the items.
    """
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}/")
async def read_item(item_id: str, needy: str, skip: int  = 0, q: str | None = None):
    """
    Endpoint to read an item by its ID.

    Args:
        item_id (int): The ID of the item.
        q (str, optional): A query parameter.

    Returns:
        dict: A dictionary containing the item ID.
        :param needy:
    """
    print(q)
    if q:
        return {"item_id": item_id, "q": q, "needy": needy}
    return {"item_id": item_id, "needy": needy, "skip": skip}



@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    """
    Endpoint to read a specific item for a specific user.

    Args:
        user_id (int): The ID of the user.
        item_id (str): The ID of the item.
        q (str, optional): A query parameter.
        short (bool, optional): A flag to return a short description.

    Returns:
        dict: A dictionary containing the item details.
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item