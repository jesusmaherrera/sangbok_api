from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_session
from app.crud import section as crud
from app.crud import song as song_crud
from app.schemas.section import SectionCreate, SectionRead, SectionUpdate

router = APIRouter(prefix="/songs/{song_id}/sections", tags=["sections"])


@router.get("/", response_model=List[SectionRead])
def list_sections(song_id: int, session: Session = Depends(get_session)):
    if not song_crud.get_song(session, song_id):
        raise HTTPException(status_code=404, detail="Song not found")
    return crud.get_sections(session, song_id)


@router.post("/", response_model=SectionRead, status_code=status.HTTP_201_CREATED)
def create_section(song_id: int, data: SectionCreate, session: Session = Depends(get_session)):
    if not song_crud.get_song(session, song_id):
        raise HTTPException(status_code=404, detail="Song not found")
    return crud.create_section(session, song_id, data)


@router.patch("/{section_id}", response_model=SectionRead)
def update_section(song_id: int, section_id: int, data: SectionUpdate, session: Session = Depends(get_session)):
    section = crud.get_section(session, section_id)
    if not section or section.song_id != song_id:
        raise HTTPException(status_code=404, detail="Section not found")
    return crud.update_section(session, section, data)


@router.delete("/{section_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_section(song_id: int, section_id: int, session: Session = Depends(get_session)):
    section = crud.get_section(session, section_id)
    if not section or section.song_id != song_id:
        raise HTTPException(status_code=404, detail="Section not found")
    crud.delete_section(session, section)
