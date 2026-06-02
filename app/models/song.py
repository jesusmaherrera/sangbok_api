from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from .tag import Tag, SongTag

if TYPE_CHECKING:
    from .section import Section


class Song(SQLModel, table=True):
    __tablename__ = "song"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    artist: Optional[str] = None
    key: Optional[str] = None
    capo: int = Field(default=0)
    tempo: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    sections: List["Section"] = Relationship(back_populates="song")
    tags: List[Tag] = Relationship(back_populates="songs", link_model=SongTag)
