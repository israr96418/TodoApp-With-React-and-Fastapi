from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import setting

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()
sqlalchemy_database_url =f"mysql+mysqldb://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"

engine = create_engine(sqlalchemy_database_url)

sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()