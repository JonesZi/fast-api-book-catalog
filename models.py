from pydantic import BaseModel
from typing import Optional

class Book (BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None
    year: Optional[int] = None

