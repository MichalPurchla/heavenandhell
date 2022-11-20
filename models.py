from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Stdent(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(50))