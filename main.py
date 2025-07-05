from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config_loader import settings

from auth.routes.auth_router import auth_router
from user.routes.user_router import user_router
from bon.routes.bon_router import bon_router

openapi_tags = [
    {
        "name": "Users",
        "description": "User operations",
    },
    {
        "name": "Auth",
        "description": "Authentication operations",
    },
    {
        "name": "Bons",
        "description": "Gestion émis auprès des fournisseurss",
    },
    {
        "name": "Health Checks",
        "description": "Application health checks",
    }
]

app = FastAPI(
        openapi_tags=openapi_tags,
        title="KisarrWeb Backend API",
        description="KisarrWeb is a web application for managing your personal finances, including income, expenses, and bills.",
        version="1.0.0",
        contact={
            "name": "KisarrWeb Team",
            "email": "kisarrweb@gmail.com"
            
            },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/license/mit/"
        },
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(auth_router, prefix='/api')
app.include_router(user_router, prefix='/api', tags=['Users'])
app.include_router(bon_router, prefix='/api', tags=['Bons'])

@app.get("/health", tags=['Health Checks'])
def read_root():
    return {"health": "true"}

