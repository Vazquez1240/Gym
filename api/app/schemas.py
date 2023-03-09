from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id:int
    name:str
    surname:str
    username:str
    password:str
    number_phone:Optional[int]
    mail:str
    state:bool
    creation:datetime = datetime.now()

class Administrador(BaseModel):
    id:int
    name:str
    surname:str
    username:str
    password:str
    number_phone:int
    mail:str
    state:bool
    range:str
    creation: datetime = datetime.now()

class UserId(BaseModel):
    id:int