from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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