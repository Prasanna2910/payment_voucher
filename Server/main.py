# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.post("/create_voucher")
def create_voucher(voucher_data: dict):
    return {"message": "Voucher created successfully", "data": voucher_data}    
