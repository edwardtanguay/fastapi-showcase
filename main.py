from fastapi import FastAPI

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

BOOKS = [
	{
		"id": 1,
		"title": "Homo Sapiens",
		"completed": True
	},
	{
		"id": 2,
		"title": "Homo Deus",
		"completed": True
	},
	{
		"id": 3,
		"title": "Nexus",
		"completed": False
	}
]

@app.get("/books")
async def get_books(completed: bool):
	filtered_books = list(filter(lambda book: book["completed"] == completed, BOOKS))
	return filtered_books