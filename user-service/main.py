from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock data
users = []

class User(BaseModel):
    name: str
    email: str

@app.get("/users")
def list_users():
    return users

@app.post("/users")
def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }
    users.append(new_user)
    return new_user
