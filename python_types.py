from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Aldmiro Passagem"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2024-05-07 06:40",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)

print(user)
print(user.id)

def get_fullname(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_fullname("Aldmiro", "Passagem"))
