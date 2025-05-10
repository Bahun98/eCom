from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock data
products = [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Phone"}]

class Product(BaseModel):
    name: str

@app.get("/products")
def list_products():
    return products

@app.post("/products")
def add_product(product: Product):
    new_product = {"id": len(products) + 1, "name": product.name}
    products.append(new_product)
    return new_product
