from fastapi import FastAPI
from pydantic import BaseModel
db = []

app = FastAPI()


class Person(BaseModel):
    first: str
    last: str


@app.get("/")
def first():
    return ("yay fastApi is sleek")


@app.get("/persons")
def getall():
    return db


@app.get("/persons/{id}")
def getone(id: int):
    return db[id-1]


@app.post("/persons")
def create(person: Person):
    db.append(person.dict())
    return db[-1]


@app.delete("/persons/{id}")
def delete_person(id: int):
    db.pop(id - 1)
    return ("successfully deleted user")
