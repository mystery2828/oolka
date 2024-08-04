from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import Event, EventCreate, BookingCreate
from app.service import event_service

router = APIRouter()

@router.get("/events", response_model=list[Event])
def get_events(db: Session = Depends(get_db)):
    return event_service.get_all_events(db)

@router.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = event_service.get_event_by_id(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/events", response_model=Event)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return event_service.create_new_event(db, event)

@router.post("/events/{event_id}/book")
def book_tickets(event_id: int, booking: BookingCreate, db: Session = Depends(get_db)):
    booking.event_id = event_id
    result = event_service.book_event_tickets(db, booking)
    if result is None:
        raise HTTPException(status_code=400, detail="Insufficient tickets available")
    return result
