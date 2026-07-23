from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import get_db
from schemas import Application

app = FastAPI()
DbSession = Annotated[Session,Depends(get_db)]

@app.get("/applications", response_model=list[Application])
def read_applications(db: DbSession):
    return db.query(models.Application).all()


@app.post("/applications", status_code=status.HTTP_201_CREATED, response_model=Application)
def add_application(application: Application, db: DbSession):
    db_application = models.Application(**application.model_dump())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


@app.delete("/applications/{id}")
def delete_application(id: int, db: DbSession):
    application = find_application(id, db)
    db.delete(application)
    db.commit()


@app.patch("/applications/{id}", response_model=Application)
def update_status(id: int, newState: models.StatusEnum, db: DbSession):
    application = find_application(id, db)
    application.state = newState  # type: ignore
    db.commit()
    db.refresh(application)
    return application


def find_application(id: int, db: Session):
    application = (
        db.query(models.Application).filter(models.Application.id == id).first()
    )
    if not application:
        raise HTTPException(status_code=404, detail="Application not Found")
    return application
