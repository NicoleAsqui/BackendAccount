from fastapi import FastAPI
from app.adapters.api import account_controller
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

origins = os.getenv("URL", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_controller.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Bank API"}
