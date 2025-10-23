
# from pydantic import BaseModel, Field
# from typing import Optional

# class GenerateRequest(BaseModel):
#     topic: str = Field(min_length=3)
#     keywords: Optional[str] = ''
#     tone: str = 'informative'
#     audience: str
#     word_count: int = 800

# class GenerateResponse(BaseModel):
#     content: str

# class DraftCreate(BaseModel):
#     topic: Optional[str] = None
#     keywords: Optional[str] = None
#     tone: Optional[str] = None
#     audience: Optional[str] = None
#     word_count: Optional[int] = None
#     content: str
#     status: Optional[str] = 'draft'

# class DraftOut(BaseModel):
#     id: int
#     topic: Optional[str]
#     keywords: Optional[str]
#     tone: Optional[str]
#     audience: Optional[str]
#     word_count: Optional[int]
#     content: str
#     status: str
#     created_at: str
#     updated_at: str
#     class Config:
#         from_attributes = True

# app/schemas.py
# from pydantic import BaseModel, Field
# from typing import Optional, Literal
# from datetime import datetime

# class GenerateRequest(BaseModel):
#     topic: str = Field(min_length=3)
#     keywords: Optional[str] = ''
#     tone: Literal['informative', 'conversational', 'professional', 'casual', 'persuasive'] = 'informative'
#     audience: str
#     word_count: int = Field(default=800, ge=200, le=2000)

# class GenerateResponse(BaseModel):
#     content: str

# class DraftCreate(BaseModel):
#     topic: Optional[str] = None
#     keywords: Optional[str] = None
#     tone: Optional[str] = None
#     audience: Optional[str] = None
#     word_count: Optional[int] = Field(default=None, ge=100, le=5000)  # broader range for drafts
#     content: str
#     status: Optional[str] = 'draft'

# class DraftOut(BaseModel):
#     id: int
#     topic: Optional[str]
#     keywords: Optional[str]
#     tone: Optional[str]
#     audience: Optional[str]
#     word_count: Optional[int]
#     content: str
#     status: str
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         from_attributes = True  # for Pydantic v2


# app/schemas.py
from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class GenerateRequest(BaseModel):
    topic: str = Field(min_length=3)
    keywords: Optional[str] = ''
    tone: Literal['informative', 'conversational', 'professional', 'casual', 'persuasive'] = 'informative'
    audience: str
    word_count: int = Field(default=800, ge=200, le=2000)

class GenerateResponse(BaseModel):
    content: str

class DraftCreate(BaseModel):
    topic: Optional[str] = None
    keywords: Optional[str] = None
    tone: Optional[str] = None
    audience: Optional[str] = None
    word_count: Optional[int] = Field(default=None, ge=100, le=5000)
    content: str
    status: Optional[str] = 'draft'

class DraftOut(BaseModel):
    id: int
    topic: Optional[str]
    keywords: Optional[str]
    tone: Optional[str]
    audience: Optional[str]
    word_count: Optional[int]
    content: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True