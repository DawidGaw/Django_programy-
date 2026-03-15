from pydantic import BaseModel
from typing import List, Optional

class BookResponse(BaseModel):
    title: str
    authors: List[str]
    published_date: Optional[str]
    categories: Optional[List[str]]
    average_rating: Optional[float]
    ratings_count: Optional[int]
    thumbnail: Optional[str]

    class Config:
        orm_mode = True