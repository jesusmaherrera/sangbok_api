from sqlmodel import SQLModel
from app.models.section import SectionType


class SectionCreate(SQLModel):
    type: SectionType
    order: int
    content: str


class SectionRead(SQLModel):
    id: int
    song_id: int
    type: SectionType
    order: int
    content: str


class SectionUpdate(SQLModel):
    type: SectionType | None = None
    order: int | None = None
    content: str | None = None
