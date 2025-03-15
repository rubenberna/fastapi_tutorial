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


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Endpoint to read an item by its ID.

    Args:
        item_id (int): The ID of the item.

    Returns:
        dict: A dictionary containing the item ID.
    """
    return {"item_id": item_id}


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