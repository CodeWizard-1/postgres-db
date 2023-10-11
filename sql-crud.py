from sqlalchemy import (
    create_engine, Column, Float, ForeugnKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# execuring the instruction from the "chibook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()