from uuid import UUID
from fastapi import FastAPI, HTTPException
from Models.Books import BooksModel

app = FastAPI()

example_data = {"data": {"message": "Hello world"}}
booksArray = []


@app.get("/")
def get_root():
    """Root route, sending an example nested dictionary body of data"""
    return example_data

@app.get("/dynamic/{name}")
def get_dynamic_path_by_name(name:str):
    """A dynamic route that will return a message based on the route path parameter"""
    copy_of_example_data = example_data
    copy_of_example_data["data"].update({"message": name})
    return copy_of_example_data

@app.get("/books/all")
def get_books():
    """Gets all book entries"""
    return booksArray

@app.post("/books/create")
def create_books(book_data:BooksModel):
    """Creates a new book entry"""
    booksArray.append(book_data)
    return booksArray

@app.put("/books/{book_id}")
def update_books_by_id(book_id: UUID, updated_book:BooksModel):
    """updates an existing book entry by a matching ID"""
    for book in booksArray:
        i = 0
        if book.id == book_id:
            booksArray[i] = updated_book
            # if the id is not updated in the updated_book, it is added here instead.
            booksArray[i].id = book_id
            return booksArray[i]
        i += 1
    raise HTTPException(
        status_code=404,
        detail= f"ID {book_id} : does not exist"
    )

@app.delete("/books/{book_id}")
def delete_book_by_id(book_id: UUID):
    """Delete book by id"""
    for book in booksArray:
        i = 0
        if book.id == book_id:
            deleted_book = booksArray[i]
            del booksArray[i]
            return deleted_book
        i += 1
