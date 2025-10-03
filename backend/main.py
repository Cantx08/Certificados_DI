from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sistema de Publicaciones y Certificaciones de Scopus EPN",
    description="API para consulta de publicaciones de Scopus.",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Endpoint de salud."""
    return {"status": "healthy", "message": "API funcionando correctamente"}
