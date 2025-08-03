from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Formato: mysql+pymysql://user:password@host/dbname
DATABASE_URL = "mysql+pymysql://root:@localhost/documentDB"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Crear una instancia DeclarativeMeta
Base = declarative_base()

# Crear la clase SessionLocal desde el factory sessionmaker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)