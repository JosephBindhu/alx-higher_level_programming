#!/usr/bin/python3
"""
The script defines a city class to
work with MySQLAlchemy ORM. 
"""
from model_state import Base, State
from sqlalchemy import  column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __table__ (str): The table name of the class
        id (int): The id name of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """
    __table__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
