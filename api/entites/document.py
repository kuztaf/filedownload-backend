from pydantic import BaseModel
from api.enum.FileTypeEnum import FileTypeEnum

class Document(BaseModel):
    id: int
    title: str
    content: bytes
    type: FileTypeEnum  
    owner_id: int

    class Config:
        orm_mode = True