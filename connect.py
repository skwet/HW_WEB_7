from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


db_name = config.get("DB", "NAME")
password = config.get("DB", "PASS")
user = config.get("DB", "USER")


# def connect():
url = f"postgresql://{user}:{password}@localhost/{db_name}"
engine = create_engine(url)
engine.connect()
DBSession = sessionmaker(bind=engine)
session = DBSession()
