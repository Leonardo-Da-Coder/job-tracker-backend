from pydantic import BaseModel
from models import StatusEnum
from datetime import date

class ApplicationCreate(BaseModel):
    company:str
    position: str
    state: StatusEnum
    applied_at: date

class Application(ApplicationCreate):
    id: int
