from datetime import datetime, timezone
from typing import Optional, List

from pydantic import (BaseModel,
                      EmailStr,
                      PastDate,
                      computed_field,
                      Field, PositiveInt, ConfigDict)

from userprofile.orm import Role

import photo.model as photo_models
import comment.model as comment_models


class UserAuthModel(BaseModel):
    """
    Model that is used to meet OAuth2 requirements
    """
    username: str
    password: str


class UserDBModel(UserAuthModel):
    """
    Model that stores user data in DB
    """
    id: PositiveInt
    hashed_pwd: str = Field(max_length=255)
    registered_at: datetime = Field(default=datetime.now(timezone.utc))

    class Config:
        orm_mode = True


class UserProfileModel(BaseModel):
    """
    Model that holds all user information
    """
    username: str
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    birthday: Optional[PastDate]
    registered_at: datetime = Field(default=datetime.now(timezone.utc))
    role: Role = Field(default='user')
    photos: Optional[List[photo_models.PhotoModel]] = []
    comments: Optional[List[comment_models.CommentModel]] = []

    @computed_field
    @property
    def full_name(self) -> str:
        """
        Fields value is computed by concatenation of first_name
        and not empty last_name

        Returns:
            str: Full name
        """
        lname = ' ' + self.last_name if self.last_name else ''
        return self.first_name + lname


class UserEditableProfileModel(BaseModel):
    """
    Model that holds all user information
    """
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    birthday: Optional[PastDate]


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    email_token: str
    token_type: str = "bearer"


class UserPublicProfileModel(BaseModel):
    """
    Model that holds public user information
    """
    model_config = ConfigDict(from_attributes=True)
    username: str
    first_name: str
    last_name: Optional[str]
    registered_at: datetime = Field(default=datetime.now(timezone.utc))
    role: Role = Field(default='user')
    photos: int = Field(ge=0, default=0)
    comments: int = Field(ge=0, default=0)

    @computed_field
    @property
    def full_name(self) -> str:
        """
        Fields value is computed by concatenation of first_name
        and not empty last_name

        Returns:
            str: Full name
        """
        lname = ' ' + self.last_name if self.last_name else ''
        return self.first_name + lname
