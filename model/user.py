from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column("id", Integer, primary_key=True)
    first_name = Column("first_name", String, unique=True)
    last_name = Column("last_name", String, nullable=False)
    cpf = Column("cpf", String, nullable=False)
    birth_date = Column("birth_date", String, nullable=False)
    date_insertion = Column(DateTime, default=datetime.now())

    def __init__(self, first_name: String, last_name: String, cpf: String, birth_date: String, date_insertion: Union[DateTime, None] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.birth_date = birth_date

        if date_insertion:
            self.date_insertion = date_insertion

    def jsonified_exercise(self, ):
        return {
            "day_serie": self.day_serie,
            "name": self.name,
            "muscle_group": self.muscle_group,
            "series": self.series,
            "series_repeats": self.series_repeats
        }
