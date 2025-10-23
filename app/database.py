
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from .config import settings

# engine = create_engine(settings.DATABASE_URL, echo=False, future=True)
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# Base = declarative_base()

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from .config import settings

# # Use the DATABASE_URL from .env via settings
# engine = create_engine(settings.DATABASE_URL, echo=True, future=True)

# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# Base = declarative_base()

# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings
engine = create_engine(settings.DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

