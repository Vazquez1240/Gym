from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    name:str
    surname:str
    username:str
    password:str
    number_phone:Optional[int]
    mail:str
    creation:datetime = datetime.now()

class Administrador(BaseModel):
    name:str
    surname:str
    username:str
    password:str
    number_phone:int
    mail:str
    rango:str
    creation: datetime = datetime.now()

class UserId(BaseModel):
    id:int