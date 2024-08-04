# app/routers/event_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import Event, EventCreate, BookingCreate
from app.controller import event_controller

router = APIRouter()

@router.get("/events", response_model=list[Event])
def get_events(db: Session = Depends(get_db)):
    return event_controller.handle_get_all_events(db)

@router.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    return event_controller.handle_get_event_by_id(db, event_id)

@router.post("/events", response_model=Event)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return event_controller.handle_create_new_event(db, event)

@router.post("/events/{event_id}/book")
def book_tickets(event_id: int, booking: BookingCreate, db: Session = Depends(get_db)):
    return event_controller.handle_book_event_tickets(db, event_id, booking)
