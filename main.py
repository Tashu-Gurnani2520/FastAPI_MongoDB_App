from fastapi import FastAPI
from routes.auth import auth_router
from routes.products import products_router
from routes.cart import cart_router
from routes.orders import orders_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(products_router, prefix="/products")
app.include_router(cart_router, prefix="/cart")
app.include_router(orders_router, prefix="/orders")

@app.get("/")
async def root():
    return {"msg": "Welcome to the E-Commerce API"}
