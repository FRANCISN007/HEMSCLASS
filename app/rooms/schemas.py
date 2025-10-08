from pydantic import BaseModel

class RoomBase(BaseModel):
    room_number: str
    type: str
    price: float
    status: str | None = "available"

class RoomCreate(RoomBase):
    pass

class RoomUpdate(BaseModel):
    room_number: str | None = None
    type: str | None = None
    price: float | None = None
    status: str | None = None

class Room(RoomBase):
    id: int
    class Config:
        from_attributes = True
