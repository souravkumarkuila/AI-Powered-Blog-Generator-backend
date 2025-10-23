
# from fastapi import APIRouter, HTTPException
# from ..schemas import GenerateRequest, GenerateResponse
# from ..services.azure_openai import generate_blog

# router = APIRouter(prefix='/api', tags=['generate'])

# @router.post('/generate', response_model=GenerateResponse)
# async def generate(req: GenerateRequest):
#     try:
#         content = generate_blog(req.topic, req.keywords or '', req.tone, req.audience, min(max(req.word_count, 200), 2000))
#         return { 'content': content }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# app/routers/generate.py
from fastapi import APIRouter, HTTPException
from ..schemas import GenerateRequest, GenerateResponse
from ..services.azure_openai import generate_blog

router = APIRouter(prefix='/api', tags=['generate'])

@router.post('/generate', response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    try:
        wc = max(200, min(req.word_count, 2000))
        content = generate_blog(req.topic, req.keywords or '', req.tone, req.audience, wc)
        return {'content': content}
    except Exception:
        raise HTTPException(status_code=500, detail='Generation failed')