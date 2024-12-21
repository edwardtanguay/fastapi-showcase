import time
from enum import Enum
from fastapi import FastAPI, Request
from routers import books, flashcards

class Tags(Enum):
    home: str = "Home",
    books: str = "Books"
    flashcards: str = "Flashcards"

app = FastAPI()
app.title = "Info API"

app.include_router(books.router, tags=[Tags.books])
app.include_router(flashcards.router, tags=[Tags.flashcards])

@app.middleware("http")
async def add_process_time_header (request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    total_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(total_time)
    return response

@app.get("/", tags=[Tags.home])
async def info():
    return {}