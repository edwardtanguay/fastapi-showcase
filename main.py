from typing import Union
from fastapi import FastAPI
from data import BOOKS

app = FastAPI()
app.title = "Hello World API"

@app.get("/")
async def hello_world():
	return {"message": "hello world"}

@app.get("/flashcards")
async def get_flashcards():
	return [
		{
			"id": 1,
			"front": "house",
			"back": "das Haus"
		},
		{
			"id": 2,
			"front": "tree",
			"back": "der Baum"
		}
	]

@app.get("/books")
async def get_books(completed: Union[bool, None] = None):
	if completed is not None:
		filtered_books = list(filter(lambda book: book["completed"] == completed, BOOKS))
		return filtered_books
	return BOOKS