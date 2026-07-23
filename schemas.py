from datetime import date

from pydantic import BaseModel

from models import StatusEnum


class Application(BaseModel):
    id: int | None = None
    company: str
    position: str
    state: StatusEnum
    applied_at: date

    class Config:
        from_attributes = True
