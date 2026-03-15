from django.db import models
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Books(Base):
    __tablename__ = 'books'

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    authors = Column(String)
    published_date = Column(String)
    categories = Column(String)
    average_rating = Column(Float)
    ratings_count = Column(Integer)
    thumbnail = Column(String)


