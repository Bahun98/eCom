from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Mock data
orders = []

class Order(BaseModel):
    user_id: int
    product_id: int
    quantity: int

@app.get("/orders")
def list_orders():
    return orders

@app.post("/orders")
def create_order(order: Order):
    new_order = {
        "id": len(orders) + 1,
        "user_id": order.user_id,
        "product_id": order.product_id,
        "quantity": order.quantity
    }
    orders.append(new_order)
    return new_order
