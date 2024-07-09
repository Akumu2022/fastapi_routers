from fastapi import APIRouter,HTTPException
from models.order import Order


router=APIRouter()

@router.get("/orders/{order_id}")
async def get_order(order_id:int):
    raise HTTPException(status_code=404,detail="Order not found")


@router.post("/orders/")
async def add_order(order: Order):
    return {"msg":order.dict()}

