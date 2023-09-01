from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column("id", Integer, primary_key=True)
    first_name = Column("first_name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    cpf = Column("cpf", String, nullable=False)
    birth_date = Column("birth_date", String, nullable=False)
    email = Column("email", String, nullable=False)
    password = Column("password", String, nullable=False)
    date_insertion = Column(DateTime, default=datetime.now())

    def __init__(self, first_name: String, last_name: String, cpf: String, birth_date: String, email:String, password:String, date_insertion: Union[DateTime, None] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.birth_date = birth_date
        self.email = email
        self.password = password

        if date_insertion:
            self.date_insertion = date_insertion

    def jsonified_exercise(self, ):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "cpf": self.cpf,
            "birth_date": self.birth_date,
            "email": self.email,
            "password": self.password,
            "date_inserion": self.date_insertion
        }