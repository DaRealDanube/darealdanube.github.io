from fastapi import FastAPI
from auth import router as auth_router

app = FastAPI(title="Danube Login API")

app.include_router(auth_router)
