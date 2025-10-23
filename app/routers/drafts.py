
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from ..database import SessionLocal
# from ..models import Draft
# from ..schemas import DraftCreate, DraftOut
# from typing import List

# router = APIRouter(prefix='/api', tags=['drafts'])

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post('/drafts', response_model=DraftOut)
# def create_draft(payload: DraftCreate, db: Session = Depends(get_db)):
#     draft = Draft(
#         topic=payload.topic,
#         keywords=payload.keywords,
#         tone=payload.tone,
#         audience=payload.audience,
#         word_count=payload.word_count,
#         content=payload.content,
#         status=payload.status or 'draft',
#     )
#     db.add(draft)
#     db.commit()
#     db.refresh(draft)
#     return draft

# @router.get('/drafts', response_model=List[DraftOut])
# def list_drafts(db: Session = Depends(get_db)):
#     return db.query(Draft).order_by(Draft.updated_at.desc()).all()

# @router.get('/drafts/{draft_id}', response_model=DraftOut)
# def get_draft(draft_id: int, db: Session = Depends(get_db)):
#     d = db.get(Draft, draft_id)
#     if not d:
#         raise HTTPException(status_code=404, detail='Draft not found')
#     return d

# @router.put('/drafts/{draft_id}', response_model=DraftOut)
# def update_draft(draft_id: int, payload: DraftCreate, db: Session = Depends(get_db)):
#     d = db.get(Draft, draft_id)
#     if not d:
#         raise HTTPException(status_code=404, detail='Draft not found')
#     for field, value in payload.model_dump(exclude_unset=True).items():
#         setattr(d, field, value)
#     db.add(d)
#     db.commit()
#     db.refresh(d)
#     return d

# @router.delete('/drafts/{draft_id}')
# def delete_draft(draft_id: int, db: Session = Depends(get_db)):
#     d = db.get(Draft, draft_id)
#     if not d:
#         raise HTTPException(status_code=404, detail='Draft not found')
#     db.delete(d)
#     db.commit()
#     return { 'ok': True }


# app/routers/drafts.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import SessionLocal
from ..models import Draft
from ..schemas import DraftCreate, DraftOut

router = APIRouter(prefix='/api', tags=['drafts'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/drafts', response_model=DraftOut)
def create_draft(payload: DraftCreate, db: Session = Depends(get_db)):
    draft = Draft(
        topic=payload.topic,
        keywords=payload.keywords,
        tone=payload.tone,
        audience=payload.audience,
        word_count=payload.word_count,
        content=payload.content,
        status=payload.status or 'draft',
    )
    db.add(draft)
    db.commit()
    db.refresh(draft)
    return draft

@router.get('/drafts', response_model=List[DraftOut])
def list_drafts(db: Session = Depends(get_db)):
    return db.query(Draft).order_by(Draft.updated_at.desc()).all()

@router.get('/drafts/{draft_id}', response_model=DraftOut)
def get_draft(draft_id: int, db: Session = Depends(get_db)):
    d = db.get(Draft, draft_id)
    if not d:
        raise HTTPException(status_code=404, detail='Draft not found')
    return d

@router.put('/drafts/{draft_id}', response_model=DraftOut)
def update_draft(draft_id: int, payload: DraftCreate, db: Session = Depends(get_db)):
    d = db.get(Draft, draft_id)
    if not d:
        raise HTTPException(status_code=404, detail='Draft not found')
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(d, field, value)
    db.add(d)
    db.commit()
    db.refresh(d)
    return d

@router.delete('/drafts/{draft_id}')
def delete_draft(draft_id: int, db: Session = Depends(get_db)):
    d = db.get(Draft, draft_id)
    if not d:
        raise HTTPException(status_code=404, detail='Draft not found')
    db.delete(d)
    db.commit()
    return {'ok': True}
