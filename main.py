from fastapi import FastAPI
from routers import user as user_router, item as item_router, order as order_router

app=FastAPI()

app.include_router(user_router.router,prefix="/api/v1", tags=["users"])

app.include_router(item_router.router, prefix="/api/v1", tags=["items"])

app.include_router(order_router.router,prefix="/api/v1",tags=["orders"])
   
         
         
            
            
    





