from fastapi import APIRouter,HTTPException
from models.user import User

router=APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id:int):
    raise HTTPException(status_code=404,detail="User not found")


@router.post("/users/")
async def get_user(user: User):
    return {"msg":user}

