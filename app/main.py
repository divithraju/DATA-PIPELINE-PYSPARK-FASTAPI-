from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Data Pipeline API")

app.include_router(router)
