from pydantic import BaseModel
from typing import Optional, List
from bson import ObjectId

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    hashed_password: str
    role: str = "customer"  # Default role is customer

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    price: float
    stock: int
    category: str
    rating: Optional[float] = 0.0
    reviews: Optional[List[dict]] = []

class CartItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    id: Optional[str] = None
    user_id: str
    items: List[CartItem]
    total: float
    status: str = "pending"
