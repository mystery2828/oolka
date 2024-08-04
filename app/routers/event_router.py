from fastapi import APIRouter
from app.controller import event_controller

router = APIRouter()

router.include_router(event_controller.router, prefix="/events", tags=["events"])
