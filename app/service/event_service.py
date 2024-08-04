from sqlalchemy.orm import Session
from app.repository.event_repository import EventRepository
from app.schemas import EventCreate, BookingCreate

def get_all_events(db: Session):
    return EventRepository.get_events(db)

def get_event_by_id(db: Session, event_id: int):
    return EventRepository.get_event(db, event_id)

def create_new_event(db: Session, event: EventCreate):
    return EventRepository.create_event(db, event)

def book_event_tickets(db: Session, booking: BookingCreate):
    event = EventRepository.get_event(db, booking.event_id)
    if event and event.available_tickets >= booking.tickets:
        event.available_tickets -= booking.tickets
        db.commit()
        return EventRepository.book_tickets(db, booking)
    return None
