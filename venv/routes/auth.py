from fastapi import APIRouter, HTTPException, Depends
from passlib.hash import bcrypt
from database import db
from models import User
from schemas import UserCreate, UserLogin
from jose import jwt, JWTError
from datetime import datetime, timedelta

auth_router = APIRouter()

@auth_router.post("/signup")
async def signup(user: UserCreate):
    if db["users"].find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    hashed_password = bcrypt.hash(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db["users"].insert_one(new_user.dict())
    return {"msg": "User created successfully"}

@auth_router.post("/login")
async def login(user: UserLogin):
    db_user = db["users"].find_one({"email": user.email})
    if not db_user or not bcrypt.verify(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"user_id" : str(db_user["_id"]), "msg": "User logged in successfully"}
