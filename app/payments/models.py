from sqlalchemy import Column, Integer, Float, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False, default="unpaid")  # unpaid, partial, paid

    booking = relationship("Booking")
