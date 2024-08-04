# app/controllers/event_controller.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import EventCreate, BookingCreate
from app.service import event_service

def handle_get_all_events(db: Session):
    return event_service.get_all_events(db)

def handle_get_event_by_id(db: Session, event_id: int):
    event = event_service.get_event_by_id(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

def handle_create_new_event(db: Session, event: EventCreate):
    return event_service.create_new_event(db, event)

def handle_book_event_tickets(db: Session, event_id: int, booking: BookingCreate):
    booking.event_id = event_id
    result = event_service.book_event_tickets(db, booking)
    if result is None:
        raise HTTPException(status_code=400, detail="Insufficient tickets available")
    return result
