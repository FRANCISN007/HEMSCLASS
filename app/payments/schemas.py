from pydantic import BaseModel
import datetime

class PaymentBase(BaseModel):
    booking_id: int
    amount_paid: float
    payment_date: datetime.date
    status: str | None = "unpaid"

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    booking_id: int | None = None
    amount_paid: float | None = None
    payment_date: datetime.date | None = None
    status: str | None = None

class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True