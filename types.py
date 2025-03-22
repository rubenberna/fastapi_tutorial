from datetime import datetime
from pydantic import BaseModel
from typing import Annotated

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[str] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": ["jane", "john"],
}

user = User(**external_data)

def say_hello(name: Annotated[str, "name to greet"]) -> str:
    return f"Hello, {name}"

if __name__ == "__main__":
    print(user)
    #> id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=['jane', 'john']
    print(user.id)
    print(say_hello(name="Ruben"))