from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String, nullable=False, unique=True)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="available")  # available, occupied, maintenance
