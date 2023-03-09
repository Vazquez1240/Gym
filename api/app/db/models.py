from app.db.database import Base
from sqlalchemy import Column,Integer,String,Boolean,Float,DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

'''
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
'''

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    surname = Column(String,nullable=False)
    username = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    number_phone = Column(Integer,nullable=False)
    mail = Column(String,nullable=False)
    state = Column(Boolean,default=False)
    creation = Column(DateTime,default=datetime.now,onupdate=datetime.now)


'''class Administrador(BaseModel):
    id:int
    name:str
    surname:str
    username:str
    password:str
    number_phone:int
    mail:str
    state:bool
    range:str
    creation: datetime = datetime.now()'''

class Administrador(Base):
    __tablename__ = "administrador"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    number_phone = Column(Integer, nullable=False)
    mail = Column(String, nullable=False)
    state = Column(Boolean, default=False)
    range = Column(String,nullable=False)
    creation = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    sale = relationship("Sale",backref="users",cascade="delete,merge")

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    venta = Column(Integer)
    ventas_productos = Column(Integer)
