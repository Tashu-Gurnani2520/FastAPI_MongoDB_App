from fastapi import APIRouter, Depends
from database import db
from models import CartItem

cart_router = APIRouter()

@cart_router.post("/add")
async def add_to_cart(item: CartItem, user_id: str):
    # Find existing cart or create new one
    cart = db["carts"].find_one({"user_id": user_id}) or {"user_id": user_id, "items": []}
    
    # Add new item
    cart["items"].append(item.dict())
    
    # Update cart in database
    db["carts"].update_one(
        {"user_id": user_id}, 
        {"$set": cart}, 
        upsert=True
    )
    
    # Get updated cart and convert ObjectId to string for JSON serialization
    updated_cart = db["carts"].find_one({"user_id": user_id})
    if updated_cart and "_id" in updated_cart:
        updated_cart["_id"] = str(updated_cart["_id"])  # Convert ObjectId to string
    
    return {
        "cart": updated_cart,
        "msg": "Item added to cart"
    }

@cart_router.get("/")
async def get_cart(user_id: str):
    cart = db["carts"].find_one({"user_id": user_id})
    # If cart exists, convert ObjectId to string
    if cart and '_id' in cart:
        cart['_id'] = str(cart['_id'])
    return cart or {"user_id": user_id, "items": []}
