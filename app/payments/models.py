from sqlalchemy import Column, Integer, Float, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="unpaid")
    payment_date = Column(DateTime, default=func.now())

    booking = relationship("Booking")
