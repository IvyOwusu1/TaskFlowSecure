from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)
#app = FastAPI(title="TaskFlow Secure")
# app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG)



@app.get("/")
def read_root():
    return {"APP_NAME": settings.APP_NAME, 
            "APP_VERSION": settings.APP_VERSION ,
            "status": "running",

    }

#return {"message": "Welcome to TaskFlow Secure ", 
#            "version": "0.1.0" ,
#            "status": "running"}