from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
import requests

from database import SessionLocal, engine, Base
from models import Books

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST /db
@app.post("/db")
def load_books(q: dict, db: Session = Depends(get_db)):

    query = q["q"]
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    response = requests.get(url).json()

    for item in response.get("items", []):
        info = item["volumeInfo"]

        book = db.query(Books).filter(Books.id == item["id"]).first()

        if not book:
            book = Books(id=item["id"])

        book.title = info.get("title")
        book.authors = ",".join(info.get("authors", []))
        book.published_date = info.get("publishedDate")
        book.categories = ",".join(info.get("categories", []))
        book.average_rating = info.get("averageRating")
        book.ratings_count = info.get("ratingsCount")
        book.thumbnail = info.get("imageLinks", {}).get("thumbnail")

        db.merge(book)

    db.commit()

    return {"status": "ok"}

@app.get("/books")
def get_books(
    author: list[str] | None = Query(None),
    published_date: str | None = None,
    sort: str | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(Books)

    if author:
        query = query.filter(Books.authors.in_(author))

    if published_date:
        query = query.filter(Books.published_date.contains(published_date))

    if sort:
        if sort.startswith("-"):
            query = query.order_by(getattr(Books, sort[1:]).desc())
        else:
            query = query.order_by(getattr(Books, sort))

    books = query.all()

    return books

@app.get("/books/{book_id}")
def get_book(book_id: str, db: Session = Depends(get_db)):

    book = db.query(Books).filter(Books.id == book_id).first()

    return {
        "title": book.title,
        "authors": book.authors.split(",") if book.authors else [],
        "published_date": book.published_date,
        "categories": book.categories.split(",") if book.categories else [],
        "average_rating": book.average_rating,
        "ratings_count": book.ratings_count,
        "thumbnail": book.thumbnail,
    }