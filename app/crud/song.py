from typing import List, Optional
from datetime import datetime
from sqlmodel import Session, select
from app.models import Song, Tag
from app.schemas.song import SongCreate, SongUpdate


def get_songs(session: Session, offset: int = 0, limit: int = 20) -> List[Song]:
    return session.exec(select(Song).offset(offset).limit(limit)).all()


def get_song(session: Session, song_id: int) -> Optional[Song]:
    return session.get(Song, song_id)


def create_song(session: Session, data: SongCreate) -> Song:
    tags = session.exec(select(Tag).where(Tag.id.in_(data.tag_ids))).all() if data.tag_ids else []
    song = Song.model_validate(data, update={"tags": tags})
    session.add(song)
    session.commit()
    session.refresh(song)
    return song


def update_song(session: Session, song: Song, data: SongUpdate) -> Song:
    update_data = data.model_dump(exclude_unset=True)

    if "tag_ids" in update_data:
        tag_ids = update_data.pop("tag_ids")
        song.tags = session.exec(select(Tag).where(Tag.id.in_(tag_ids))).all()

    for field, value in update_data.items():
        setattr(song, field, value)

    song.updated_at = datetime.utcnow()
    session.add(song)
    session.commit()
    session.refresh(song)
    return song


def delete_song(session: Session, song: Song) -> None:
    session.delete(song)
    session.commit()
