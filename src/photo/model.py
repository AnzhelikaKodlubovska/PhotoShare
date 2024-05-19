from typing import Optional, List
from pydantic import BaseModel, ConfigDict

import comment.model as comment_models
import tags.model as tag_models


class PhotoModel(BaseModel):
    title: str
    author_fk: int


class PhotoCreate(PhotoModel):
    pass


class PhotoUpdate(BaseModel):
    title: Optional[str] = None


class PhotoResponse(PhotoModel):
    id: int
    url: str
    comments: List[comment_models.CommentModel] = []
    tags: List[tag_models.TagModel] = []

    model_config = ConfigDict(from_attributes=True)
