from fastapi import FastAPI
from app.database import engine, Base

# Import routers
from app.users.router import router as user_router
from app.rooms.router import router as rooms_router
from app.bookings.router import router as bookings_router
from app.payments.router import router as payments_router
from app.license.router import router as license_router

# Create all tables (if not exist)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Hotel & Event Management System",
    description="An API for managing hotel operations including Bookings, Reservations, Rooms, and Payments.",
    version="1.0.0"
)

# Routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(rooms_router, prefix="/rooms", tags=["Rooms"])
app.include_router(bookings_router, prefix="/bookings", tags=["Bookings"])
app.include_router(payments_router, prefix="/payments", tags=["Payments"])
app.include_router(license_router, prefix="/license", tags=["License"])

@app.get("/")
def root():
    return {"message": "Welcome to HEMS Backend API"}
