from fastapi import APIRouter,HTTPException
from models.item import Item

router=APIRouter()

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/items/")
async def get_item(item: Item):
    return item
