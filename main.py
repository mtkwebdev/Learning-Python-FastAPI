from fastapi import FastAPI
from Models.Books import BooksModel

app = FastAPI()

example_data = {"data": {"message": "Hello world"}}
booksArray = []


@app.get("/")
def get_root():
    """Root route, sending an example nested dictionary body of data"""
    return example_data

@app.get("/{name}")
def get_dynamic_path_by_name(name:str):
    """A dynamic route that will return a message based on the route path parameter"""
    copy_of_example_data = example_data
    copy_of_example_data["data"].update({"message": name})
    return copy_of_example_data

@app.get("/books")
def get_books():
    return booksArray

@app.post("/books")
def create_books(bookData:BooksModel):
    booksArray.append(bookData)
    return booksArray

# @app.put("/books")
# def update_books(bookData:BooksModel):
#     booksArray.append(bookData)
#     return booksArray
