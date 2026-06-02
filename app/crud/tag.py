from typing import List, Optional
from sqlmodel import Session, select
from app.models import Tag
from app.schemas.tag import TagCreate


def get_tags(session: Session) -> List[Tag]:
    return session.exec(select(Tag)).all()


def get_tag(session: Session, tag_id: int) -> Optional[Tag]:
    return session.get(Tag, tag_id)


def create_tag(session: Session, data: TagCreate) -> Tag:
    tag = Tag.model_validate(data)
    session.add(tag)
    session.commit()
    session.refresh(tag)
    return tag


def delete_tag(session: Session, tag: Tag) -> None:
    session.delete(tag)
    session.commit()
