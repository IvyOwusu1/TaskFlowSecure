from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.core.config import settings
from app.database.init_db import init_db

init_db()

app = FastAPI(title=settings.APP_NAME)
#app = FastAPI(title="TaskFlow Secure")
# app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG)

#Register API routers
app.include_router(auth_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"app_name": settings.APP_NAME, 
            "version": settings.APP_VERSION ,
            "status": "running",

    }

#return {"message": "Welcome to TaskFlow Secure ", 
#            "version": "0.1.0" ,
#            "status": "running"}