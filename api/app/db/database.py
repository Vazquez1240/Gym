from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Aqui se colocara la base de datos a la que te conectaras
'''Como en python no existen las constantes por convenio 
la variable que sera una constante se escribe en mayusculas'''
SQLALCHEMY_DATABSE_URL = "postgresql://postgres:123@localhost:5432/gym"
engine = create_engine(SQLALCHEMY_DATABSE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()



def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()