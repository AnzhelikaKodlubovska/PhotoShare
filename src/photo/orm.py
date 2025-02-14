from typing import List, Optional

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String


from database import Base

photo_tag_association_table = Table(
    "photo_tag",
    Base.metadata,
    Column("photo_id", ForeignKey("photos.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
)


class PhotoORM(Base):
    __tablename__ = "photos"

    # columns
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    public_id: Mapped[str] = mapped_column(String, nullable=False)
    qrcode_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    author_fk: Mapped[int] = mapped_column(ForeignKey("profiles.id", ondelete="CASCADE"))
    # relations
    author: Mapped["ProfileORM"] = relationship("ProfileORM", back_populates="photos")
    comments: Mapped[List["CommentORM"]] = relationship(back_populates="photo")
    tags: Mapped[List["TagORM"]] = relationship(secondary=photo_tag_association_table, back_populates="photos")

