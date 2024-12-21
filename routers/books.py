import asyncio
import os
from pydantic import BaseModel, Field
from typing import Annotated, Union
from fastapi import HTTPException, Path, UploadFile, APIRouter, status
from data import BOOKS

router = APIRouter(
	prefix="/book"
)

class Book(BaseModel):
	id: int
	title: str = Field(min_length=5, max_length=40)
	completed: bool = Field(default=False)


@router.get("/")
async def get_books(completed: Union[bool, None] = None):
	await asyncio.sleep(2)
	if completed is not None:
		filtered_books = list(filter(lambda book: book["completed"] == completed, BOOKS))
		return filtered_books
	return BOOKS

@router.get("/{id}")
async def get_book(id:int):
	try:
		book = next(book for book in BOOKS if book["id"] == id)
		return book
	except:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

# EXAMPLE OF POST WITHOUT MODEL
# @router.post("/book")
# async def create_book(id:int = Body(), title:str = Body(), completed:bool = Body()):
# 	BOOKS.append({
# 		"id": id,
# 		"title": title,
# 		"completed": completed
# 	})
# 	return BOOKS

@router.post("/", name="Create a book", summary="creates a book for the virtual bookcase", description="This should be used to create books for the library only. For other books, use another route.", status_code=201, deprecated=False)
async def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS

# EXAMPLE WITH FILE-ANNOTATED-FILE_SIZE
# @router.post("/book/{book_id}/image_file")
# async def upload_book_image(book_id: Annotated[int, Path()], file: Annotated[bytes, File()]):
# 	try:
# 		book_data = next(book for book in BOOKS if book["id"] == book_id)
# 		book_data["file_size"] = len(file)
# 		return book_data
# 	except:
# 		raise HTTPException(status_code=404, detail="book not found")

@router.post("/{book_id}/image_file")
async def upload_book_image(book_id: Annotated[int, Path()], file: UploadFile):
	try:
		book_data = next(book for book in BOOKS if book["id"] == book_id)
		book_data["file_name"] = file.filename
		file_content = await file.read()
		save_path = f"./uploads/{file.filename}"
		os.makedirs(os.path.dirname(save_path), exist_ok=True)
		with open(save_path, "wb") as f:
			f.write(file_content)
		return book_data
	except:
		raise HTTPException(status_code=404, detail="book not found")
