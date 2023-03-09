from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    name:str
    surname:str
    username:str
    password:str
    number_phone:Optional[str]
    mail:str
    creation:datetime = datetime.now()

class Administrador(BaseModel):
    name:str
    surname:str
    username:str
    password:str
    number_phone:str
    mail:str
    rango:str
    creation: datetime = datetime.now()

class UserId(BaseModel):
    id:int

class ShowUser(BaseModel):
    name: str
    surname: str
    username: str
    mail: str
    class Config():
        orm_mode = True