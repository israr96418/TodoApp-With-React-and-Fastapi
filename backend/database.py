from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()

sqlalchemy_database_url ="mysql+mysqldb://isrardawar:dawar96418@localhost:3306/todo"
engine = create_engine(sqlalchemy_database_url)

sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()