from typing import Optional
from sqlmodel import SQLModel, Field
from api.enum.FileTypeEnum import FileTypeEnum

class DocumentBase(SQLModel):
    title: str = Field(index=True)
    content: Optional[bytes] = Field(default=None, nullable=True)
    type: Optional[FileTypeEnum] = Field(default=None, index=True)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")


class Document(DocumentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class DocumentCreate(DocumentBase):
    title: str
    content: Optional[bytes] = None
    type: Optional[FileTypeEnum] = None
    owner_id: Optional[int] = None

class DocumentUpdate(DocumentBase):
    title: Optional[str] = None
    content: Optional[bytes] = None
    type: Optional[FileTypeEnum] = None
    owner_id: Optional[int] = None

class DocumentPublic(DocumentBase):
    title: str
    owner_id: int
    model_config = {
        "from_attributes": True
    }
