from enum import Enum
from fastapi import FastAPI
from routers import books, flashcards

class Tags(Enum):
    home: str = "Home",
    books: str = "Books"
    flashcards: str = "Flashcards"

app = FastAPI()
app.title = "Info API"

app.include_router(books.router, tags=[Tags.books])
app.include_router(flashcards.router, tags=[Tags.flashcards])

@app.get("/", tags=[Tags.home])
async def info():
    return {}