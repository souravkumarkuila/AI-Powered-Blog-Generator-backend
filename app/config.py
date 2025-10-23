
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

# class Settings(BaseModel):
#     AZURE_OPENAI_ENDPOINT: str = os.getenv('AZURE_OPENAI_ENDPOINT', '')
#     AZURE_OPENAI_API_KEY: str = os.getenv('AZURE_OPENAI_API_KEY', '')
#     AZURE_OPENAI_DEPLOYMENT: str = os.getenv('AZURE_OPENAI_DEPLOYMENT', '')
#     AZURE_OPENAI_API_VERSION: str = os.getenv('AZURE_OPENAI_API_VERSION', '')
#     DATABASE_URL: str = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:S22@@localhost:3306/GENAIblob?&allowPublicKeyRetrieval=true&serverTimezone=UTC')
#     CORS_ORIGINS: str = os.getenv('CORS_ORIGINS', 'http://localhost:5173')

# class Settings(BaseModel):
#     AZURE_OPENAI_ENDPOINT: str = os.getenv('AZURE_OPENAI_ENDPOINT', '')
#     AZURE_OPENAI_API_KEY: str = os.getenv('AZURE_OPENAI_API_KEY', '')
#     AZURE_OPENAI_DEPLOYMENT: str = os.getenv('AZURE_OPENAI_DEPLOYMENT', '')
#     AZURE_OPENAI_API_VERSION: str = os.getenv('AZURE_OPENAI_API_VERSION', '')
#     DATABASE_URL: str = os.getenv('DATABASE_URL', 'mysql+pymysql://root:Sourav1999@127.0.0.1:3306/ai_blog?charset=utf8mb4')
#     CORS_ORIGINS: str = os.getenv('CORS_ORIGINS', 'http://localhost:5173')

# settings = Settings()


# from pydantic import BaseModel
# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Settings(BaseModel):
#     AZURE_OPENAI_ENDPOINT: str = os.getenv('AZURE_OPENAI_ENDPOINT', '')
#     AZURE_OPENAI_API_KEY: str = os.getenv('AZURE_OPENAI_API_KEY', '')
#     AZURE_OPENAI_DEPLOYMENT: str = os.getenv('AZURE_OPENAI_DEPLOYMENT', '')
#     AZURE_OPENAI_API_VERSION: str = os.getenv('AZURE_OPENAI_API_VERSION', '')
#     DATABASE_URL: str = os.getenv('DATABASE_URL', 'mysql+pymysql://root:Sourav1999@127.0.0.1:3306/ai_blog?charset=utf8mb4')
#     CORS_ORIGINS: str = os.getenv('CORS_ORIGINS', 'http://localhost:5173')

# settings = Settings()

# app/config.py
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    AZURE_OPENAI_ENDPOINT: str = os.getenv('AZURE_OPENAI_ENDPOINT', '')
    AZURE_OPENAI_API_KEY: str = os.getenv('AZURE_OPENAI_API_KEY', '')
    AZURE_OPENAI_DEPLOYMENT: str = os.getenv('AZURE_OPENAI_DEPLOYMENT', '')
    AZURE_OPENAI_API_VERSION: str = os.getenv('AZURE_OPENAI_API_VERSION', '2024-08-01-preview')
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'mysql+pymysql://root:password@127.0.0.1:3306/ai_blog?charset=utf8mb4')
    CORS_ORIGINS: str = os.getenv('CORS_ORIGINS', 'http://localhost:5173')

settings = Settings()
