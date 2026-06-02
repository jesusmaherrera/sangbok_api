from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import songs_router, sections_router, tags_router

app = FastAPI(title="Sangbok API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(songs_router, prefix="/api/v1")
app.include_router(sections_router, prefix="/api/v1")
app.include_router(tags_router, prefix="/api/v1")


@app.get("/health")
def health():
    return {"status": "ok"}
