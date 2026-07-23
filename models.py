from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum, Date
import enum

Base = declarative_base()

class StatusEnum(str, enum.Enum):
    applied = "applied"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    company = Column(String)
    position = Column(String)
    state = Column(Enum(StatusEnum))
    applied_at = Column(Date)
