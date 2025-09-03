from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base
from config import Config

def create_database():
    engine = create_engine(Config.DATABASE_URL)
    Base.metadata.create_all(engine)
    print("База данных и таблицы успешно созданы!")
    return engine

def get_session():
    engine = create_engine(Config.DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

engine = create_database()