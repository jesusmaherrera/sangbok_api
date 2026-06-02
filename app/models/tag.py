from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class SongTag(SQLModel, table=True):
    __tablename__ = "song_tag"

    song_id: Optional[int] = Field(default=None, foreign_key="song.id", primary_key=True)
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)


class Tag(SQLModel, table=True):
    __tablename__ = "tag"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    songs: List["Song"] = Relationship(back_populates="tags", link_model=SongTag)
