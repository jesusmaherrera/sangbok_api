from typing import Optional, TYPE_CHECKING
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .song import Song


class SectionType(str, Enum):
    verse = "verse"
    chorus = "chorus"
    bridge = "bridge"
    intro = "intro"
    outro = "outro"


class Section(SQLModel, table=True):
    __tablename__ = "section"

    id: Optional[int] = Field(default=None, primary_key=True)
    song_id: int = Field(foreign_key="song.id", index=True)
    type: SectionType
    order: int
    content: str

    song: Optional["Song"] = Relationship(back_populates="sections")
