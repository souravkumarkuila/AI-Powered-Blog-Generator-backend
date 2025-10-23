
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from .config import settings
# from .database import Base, engine
# from .routers import generate, drafts

# app = FastAPI(title='AI-Powered Blog Generator API')

# # CORS
# origins = [o.strip() for o in settings.CORS_ORIGINS.split(',') if o.strip()]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins or ['*'],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # DB init
# Base.metadata.create_all(bind=engine)

# # Routers
# app.include_router(generate.router)
# app.include_router(drafts.router)

# @app.get('/')
# async def root():
#     return { 'status': 'ok', 'ts': __import__('datetime').datetime.utcnow().isoformat() }

# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import Base, engine
from .routers import generate, drafts

app = FastAPI(title='AI-Powered Blog Generator API')

origins = [o.strip() for o in settings.CORS_ORIGINS.split(',') if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(generate.router)
app.include_router(drafts.router)

@app.get('/')
async def root():
    from datetime import datetime, timezone
    return {'status': 'ok', 'ts': datetime.now(timezone.utc).isoformat()}
