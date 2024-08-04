# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database
from app.controller import auth_controller
from app.service import auth_service

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return auth_controller.register_user(db, user)

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(database.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return auth_controller.login_for_access_token(db, form_data)

@router.get("/users/me", response_model=schemas.UserResponse)
def read_users_me(current_user: schemas.User = Depends(auth_service.get_current_active_user)):
    return current_user