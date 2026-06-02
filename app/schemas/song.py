from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel
from .tag import TagRead
from .section import SectionRead


class SongCreate(SQLModel):
    title: str
    artist: Optional[str] = None
    key: Optional[str] = None
    capo: int = 0
    tempo: Optional[int] = None
    tag_ids: List[int] = []


class SongRead(SQLModel):
    id: int
    title: str
    artist: Optional[str]
    key: Optional[str]
    capo: int
    tempo: Optional[int]
    created_at: datetime
    updated_at: datetime
    tags: List[TagRead] = []


class SongReadWithSections(SongRead):
    sections: List[SectionRead] = []


class SongUpdate(SQLModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    key: Optional[str] = None
    capo: Optional[int] = None
    tempo: Optional[int] = None
    tag_ids: Optional[List[int]] = None
