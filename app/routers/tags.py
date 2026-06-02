from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_session
from app.crud import tag as crud
from app.schemas.tag import TagCreate, TagRead

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/", response_model=List[TagRead])
def list_tags(session: Session = Depends(get_session)):
    return crud.get_tags(session)


@router.post("/", response_model=TagRead, status_code=status.HTTP_201_CREATED)
def create_tag(data: TagCreate, session: Session = Depends(get_session)):
    return crud.create_tag(session, data)


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(tag_id: int, session: Session = Depends(get_session)):
    tag = crud.get_tag(session, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    crud.delete_tag(session, tag)
