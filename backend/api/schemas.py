from datetime import datetime
from pydantic import BaseModel


class DemoBase(BaseModel):
    name: str
    decimal_value: float
    entry_date: datetime


class DemoCreate(DemoBase):
    pass


class Demo(DemoBase):
    id: int

    class Config:
        orm_mode = True
