from pydantic import BaseModel
from typing import List
from .item import Item

class Order(BaseModel):
    id: int
    user_id: int
    items: List[Item]
