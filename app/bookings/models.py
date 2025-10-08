from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..database import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    booking_date = Column(Date, nullable=False)
    number_of_days = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="active")  # active, canceled, completed
    payment_status = Column(String, nullable=False, default="unpaid")  # unpaid, partial, paid

    user = relationship("User")
    room = relationship("Room")
