from fastapi import FastAPI
from routers import user as user_router

app=FastAPI()

app.include_router(user_router.router,prefix="/api/v1", tags=["users"])

    
   
         
         
            
            
    





