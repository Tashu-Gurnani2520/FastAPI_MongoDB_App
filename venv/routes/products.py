from fastapi import APIRouter, HTTPException, Depends
from database import db
from schemas import ProductCreate
from models import Product

products_router = APIRouter()

@products_router.post("/add", tags=["Admin"])
async def add_product(product: ProductCreate, role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can add products")
    
    # Insert the product and get the inserted ID
    result = db["products"].insert_one(product.dict())
    
    # Fetch the complete product document
    created_product = db["products"].find_one({"_id": result.inserted_id})
    
    # Convert ObjectId to string for JSON serialization
    if created_product and "_id" in created_product:
        created_product["_id"] = str(created_product["_id"])
    
    return {
        "msg": "Product added successfully",
        "product": created_product
    }

from bson import ObjectId

@products_router.get("/", tags=["Public"])
async def get_products(search: str = None):
    query = {}
    if search:
        # Search in the product description for the given search word, case-insensitive
        query["description"] = {"$regex": search, "$options": "i"}
    
    # Fetch products from the database
    products = list(db["products"].find(query))
    
    # Convert ObjectId to string
    for product in products:
        product["_id"] = str(product["_id"])  # Convert ObjectId to string
    
    return products


