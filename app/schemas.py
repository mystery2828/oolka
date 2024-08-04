from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    name: str
    date: datetime
    location: str
    available_tickets: int
    description: str
    artist: str
    event_type: str
    price: float
    is_active:  Optional[bool] = True
    meta: Optional[dict] = {}
    soft_delete: Optional[bool] = False


class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    event_id: int
    user_id: int
    tickets: int
    transaction_id: Optional[str] = None
    payment_status: str
    soft_delete: Optional[bool] = False


class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None