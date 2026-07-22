from fastapi import FastAPI , status
from pydantic import BaseModel

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

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/applications")
def read_applications():
    return applications

@app.post("/applications", status_code=status.HTTP_201_CREATED)
def add_application(application: Application):
    applications.append(application)
    return application
