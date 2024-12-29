from fastapi import APIRouter, HTTPException
from database import db
from models import Order, CartItem
from bson import ObjectId
orders_router = APIRouter()

@orders_router.post("/create")
async def create_order(user_id: str):
    # Get cart
    cart = db["carts"].find_one({"user_id": user_id})
    if not cart or not cart["items"]:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # Debug print
    print("Cart contents:", cart)
    
    # Calculate total with proper ObjectId conversion and error handling
    total = 0
    invalid_products = []
    valid_items = []
    
    for item in cart["items"]:
        print(f"Processing item: {item}")  # Debug print
        
        # Convert string product_id to ObjectId
        try:
            product_id = ObjectId(item["product_id"])
            print(f"Converted ObjectId: {product_id}")  # Debug print
        except Exception as e:
            print(f"Error converting ObjectId: {e}")  # Debug print
            invalid_products.append(item["product_id"])
            continue
            
        # Find product and calculate subtotal
        product = db["products"].find_one({"_id": product_id})
        print(f"Found product: {product}")  # Debug print
        
        if not product:
            invalid_products.append(item["product_id"])
            continue
            
        total += item["quantity"] * product["price"]
        valid_items.append(item)

    # Create and save order
    new_order = Order(user_id=user_id, items=valid_items, total=total)
    result = db["orders"].insert_one(new_order.dict())
    print(f"Order created with ID: {result.inserted_id}")  # Debug print
    
    # Clear cart
    db["carts"].delete_one({"user_id": user_id})
    
    return {"msg": "Order created successfully", "order": new_order}
