from fastapi import FastAPI , status, HTTPException
from pydantic import BaseModel
import database

class Application(BaseModel):
    firma: str
    position: str
    status: str
    datum: str

applications = [
    Application(firma="DSV", position="Fullstack Entwickler", status="beworben", datum="20.07.2026"),
    Application(firma="hiqs", position="Junior Go Developer", status="beworben", datum="20.07.2026"),
    Application(firma="BAUHAUS", position="Junior Softwareentwickler", status="beworben", datum="20.07.2026"),
]

app = FastAPI()

@app.get("/applications")
def read_applications():
    return applications

@app.post("/applications", status_code=status.HTTP_201_CREATED)
def add_application(application: Application):
    applications.append(application)
    return application

@app.delete("/applications/{firma}", status_code=status.HTTP_200_OK)
def delete_application(firma:str):
    application = find_application(firma)
    applications.remove(application)

@app.patch("/applications/{firma}")
def update_status(firma:str , status:str):
    application = find_application(firma)
    application.status = status

def find_application(firma:str):
    application = next((a for a in applications if a.firma == firma ), None)
    if not application:
        raise HTTPException(status_code=404, detail="Application not Found")
    return application
