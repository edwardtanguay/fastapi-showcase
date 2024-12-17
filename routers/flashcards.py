from fastapi import APIRouter

router = APIRouter(
	prefix="/flashcard"
)

@router.get("/")
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
