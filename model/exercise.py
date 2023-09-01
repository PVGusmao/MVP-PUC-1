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
    video_exercise = Column("video_exercise", String)
    series = Column("series", Integer, nullable=False)
    series_repeats = Column("series_repeats", Integer, nullable=False)
    identify = Column("identify", Integer, nullable=False)
    user_id = Column("user_id", Integer, nullable=False)
    date_insertion = Column(DateTime, default=datetime.now())

    def __init__(self, day_serie: String, name: String, muscle_group: String, video_exercise: String, series: Integer, series_repeats: Integer, identify: Integer, user_id: Integer ,date_insertion: Union[DateTime, None] = None):
        self.day_serie = day_serie
        self.name = name
        self.muscle_group = muscle_group
        self.video_exercise = video_exercise
        self.series = series
        self.series_repeats = series_repeats
        self.identify = identify
        self.user_id = user_id

        if date_insertion:
            self.date_insertion = date_insertion

    def jsonified_exercise(self, ):
        return {
            "day_serie": self.day_serie,
            "name": self.name,
            "muscle_group": self.muscle_group,
            "video_exercise": self.video_exercise,
            "series": self.series,
            "series_repeats": self.series_repeats,
            "identify": self.identify,
            "user_id": self.user_id
        }