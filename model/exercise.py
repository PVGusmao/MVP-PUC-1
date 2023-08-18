from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Exercises(Base):
    __tablename__ = 'exercises'

    id = Column("id", Integer, primary_key=True)
    day_serie = Column("day_serie", String, unique=True)
    name = Column("name", String, nullable=False)
    muscle_group = Column("muscle_group", String, nullable=False)
    series = Column("series", Integer, nullable=False)
    series_repeats = Column("series_repeats", Integer, nullable=False)
    date_insertion = Column(DateTime, default=datetime.now())

    def __init__(self, day_serie: String, name: String, muscle_group: String, series: Integer, series_repeats: Integer, date_insertion: Union[DateTime, None] = None):
        self.day_serie = day_serie
        self.name = name
        self.muscle_group = muscle_group
        self.series = series
        self.series_repeats = series_repeats

        if date_insertion:
            self.date_insertion = date_insertion
