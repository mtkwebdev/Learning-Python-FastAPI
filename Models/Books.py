"""books_model Rest API models"""
from uuid import UUID
from pydantic import BaseModel, Field

class BooksModel(BaseModel):
    """Model for API's relating to Books"""
    id: UUID
    title: str = Field(min_length=3, max_length=100)
    author:str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=255)
    rating: int = Field(gt=-1, lt=101)
    