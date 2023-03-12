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


class ShowUser(BaseModel):
    name: str
    surname: str
    username: str
    mail: str
    class Config():
        orm_mode = True

class UpdateUSer(BaseModel):
    name:str = None
    surname:str = None
    username:str = None
    password:str = None
    number_phone:str = None
    mail:str = None

class ShowAdmin(BaseModel):
    name:str
    surname:str
    username:str
    number_phone:str
    mail:str
    class Config():
        orm_mode = True