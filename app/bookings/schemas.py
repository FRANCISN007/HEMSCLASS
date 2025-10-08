from pydantic import BaseModel
from datetime import date

class BookingBase(BaseModel):
    user_id: int
    room_id: int
    booking_date: date
    number_of_days: int
    status: str | None = "active"
    payment_status: str | None = "unpaid"

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    user_id: int | None = None
    room_id: int | None = None
    booking_date: date | None = None
    number_of_days: int | None = None
    status: str | None = None
    payment_status: str | None = None

class Booking(BookingBase):
    id: int
    class Config:
        from_attributes = True
