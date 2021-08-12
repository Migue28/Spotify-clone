from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.songs import router as songs_router
from app.routers.login import router as login_router

origins = ["http://localhost:8080",]

def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(songs_router)
    app.include_router(login_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = get_app()
