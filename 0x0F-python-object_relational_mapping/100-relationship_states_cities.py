#!/usr/bin/python3
"""script that prints the first State object from the database
hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Connecting"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    estado = State()
    estado.name = 'California'
    ciudad = City()
    ciudad.name = 'San Francisco'
    estado.cities.append(ciudad)
    session.add(estado)
    session.add(ciudad)
    session.commit()
    session.close()
