from typing import List, Optional
from sqlmodel import Session, select
from app.models import Section
from app.schemas.section import SectionCreate, SectionUpdate


def get_sections(session: Session, song_id: int) -> List[Section]:
    return session.exec(select(Section).where(Section.song_id == song_id).order_by(Section.order)).all()


def get_section(session: Session, section_id: int) -> Optional[Section]:
    return session.get(Section, section_id)


def create_section(session: Session, song_id: int, data: SectionCreate) -> Section:
    section = Section.model_validate(data, update={"song_id": song_id})
    session.add(section)
    session.commit()
    session.refresh(section)
    return section


def update_section(session: Session, section: Section, data: SectionUpdate) -> Section:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(section, field, value)
    session.add(section)
    session.commit()
    session.refresh(section)
    return section


def delete_section(session: Session, section: Section) -> None:
    session.delete(section)
    session.commit()
