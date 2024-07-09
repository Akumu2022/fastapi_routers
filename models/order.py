from pydantic import BaseModel
from typing import List,Optional
from .item import Item

class Order(BaseModel):
    id: int
    user_id: int
    # items:Optional [List[Item]] = None
