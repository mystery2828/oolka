from sqlalchemy.orm import Session
from app.models import Event, Booking
from app.schemas import EventCreate, BookingCreate

class EventRepository:
    
    @staticmethod
    def get_events(db: Session):
        return db.query(Event).all()

    @staticmethod
    def get_event(db: Session, event_id: int):
        return db.query(Event).filter(Event.id == event_id).first()

    @staticmethod
    def create_event(db: Session, event: EventCreate):
        db_event = Event(**event.dict())
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

    @staticmethod
    def book_tickets(db: Session, booking: BookingCreate):
        db_booking = Booking(**booking.dict())
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
