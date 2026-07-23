from typing import cast

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models
from database import get_db
from schemas import Application, ApplicationCreate

app = FastAPI()


@app.get("/applications")
def read_applications(db: Session = Depends(get_db)):
    return db.query(models.Application).all()


@app.post("/applications", status_code=status.HTTP_201_CREATED)
def add_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    db_application = models.Application(**application.model_dump())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


@app.delete("/applications/{id}")
def delete_application(id: int, db: Session = Depends(get_db)):
    application = find_application(id, db)
    db.delete(application)
    db.commit()


@app.patch("/applications/{id}")
def update_status(id: int, newState: models.StatusEnum, db: Session = Depends(get_db)):
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
