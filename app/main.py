from fastapi import FastAPI
from app.routers import profile_router
from app.routers import game_router

app = FastAPI(
    title="Steam Profile Analyzer",
    description="API para analizar perfiles públicos de Steam",
    version="1.0.0"
)

# Routers
app.include_router(profile_router.router)
app.include_router(game_router.router)

@app.get("/")
def home():
    return {
        "message": "Steam Profile Analyzer funcionando"
    }