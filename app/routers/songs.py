from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_session
from app.crud import song as crud
from app.schemas.song import SongCreate, SongRead, SongReadWithSections, SongUpdate

router = APIRouter(prefix="/songs", tags=["songs"])


@router.get("/", response_model=List[SongRead])
def list_songs(offset: int = 0, limit: int = 20, session: Session = Depends(get_session)):
    return crud.get_songs(session, offset=offset, limit=limit)


@router.post("/", response_model=SongReadWithSections, status_code=status.HTTP_201_CREATED)
def create_song(data: SongCreate, session: Session = Depends(get_session)):
    return crud.create_song(session, data)


@router.get("/{song_id}", response_model=SongReadWithSections)
def get_song(song_id: int, session: Session = Depends(get_session)):
    song = crud.get_song(session, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@router.patch("/{song_id}", response_model=SongReadWithSections)
def update_song(song_id: int, data: SongUpdate, session: Session = Depends(get_session)):
    song = crud.get_song(session, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return crud.update_song(session, song, data)


@router.delete("/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_song(song_id: int, session: Session = Depends(get_session)):
    song = crud.get_song(session, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    crud.delete_song(session, song)
