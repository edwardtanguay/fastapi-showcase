from fastapi import FastAPI
from routers import books, flashcards

app = FastAPI()
app.title = "Hello World API"

app.include_router(books.router)
app.include_router(flashcards.router)

@app.get("/")
async def info():
	return {"name": "Info API"}