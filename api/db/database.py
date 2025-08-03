from fastapi.params import Depends
from typing_extensions import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session
from fastapi import Depends

# Formato: mysql+pymysql://user:password@host/dbname
DATABASE_URL = "mysql+pymysql://root:@localhost/documentDB"

engine = create_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Crear una instancia DeclarativeMeta
Base = declarative_base()

# Crear la clase SessionLocal desde el factory sessionmaker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def get_session():
    with Session(engine) as session:
        yield session

session_dep = Annotated[Session, Depends(get_session)]  

def create_database_and_tables():
    """Crea la base de datos si no existe."""
    SQLModel.metadata.create_all(engine)