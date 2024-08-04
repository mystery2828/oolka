from fastapi import FastAPI
from app.routers import event_router, auth_router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(event_router.router)
app.include_router(auth_router.router)
