from fastapi import FastAPI

app = FastAPI(title="TaskFlow Secure")


@app.get("/")
def read_root():
    return {"message": "Welcome to TaskFlow Secure ", 
            "version": "0.1.0" ,
            "status": "running"}