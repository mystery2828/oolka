from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean, JSON
from sqlalchemy.orm import relationship
from .database import Base
import time
from datetime import datetime


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    artist = Column(String, nullable=True)
    event_type = Column(String, nullable=True)
    date = Column(DateTime)
    location = Column(String)
    available_tickets = Column(Integer)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    meta = Column(JSON, nullable=True)
    soft_delete = Column(Boolean, default=False)
    created_at = Column(DateTime,default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow ,nullable=False)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    user_id = Column(Integer)
    tickets = Column(Integer)
    transaction_id = Column(String, nullable=True)
    payment_status = Column(String, nullable=True)
    soft_delete = Column(Boolean, default=False)
