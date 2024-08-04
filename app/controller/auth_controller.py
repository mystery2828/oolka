# app/auth/controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import schemas, service

def register_user(db: Session, user: schemas.UserCreate):
    if service.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return service.create_user(db, user)

def login_for_access_token(db: Session, form_data):
    user = service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return service.create_access_token_response(user)
