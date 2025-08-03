from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel

from api.entites.document import DocumentPublic, Document, DocumentUpdate, DocumentCreate   
from api.db.database import SessionLocal, session_dep

router = APIRouter(prefix="/documents", tags=["documents"])

# Crear documento
@router.post("/", response_model=DocumentPublic)
def create_document(document: DocumentCreate, session: session_dep):
    db_document = Document.model_validate(document)
    session.add(db_document)
    session.commit()
    session.refresh(db_document)
    return db_document

# Obtener todos los documentos
@router.get("/", response_model=List[DocumentPublic])
def read_documents(session: session_dep):
    return session.query(Document).all()

# Obtener documento por ID
@router.get("/{document_id}", response_model=DocumentPublic)
def get_document(document_id: int, session: session_dep):
    document = session.query(Document).filter(Document.id == document_id).first()
    if document:
        return document
    raise HTTPException(status_code=404, detail="Document not found")

# Actualizar documento
@router.put("/{document_id}", response_model=DocumentPublic)
def update_document(document_id: int, updated_document: DocumentUpdate, session: session_dep):
    document = session.query(Document).filter(Document.id == document_id).first()
    if document:
        document_data = updated_document.dict(exclude_unset=True)
        for key, value in document_data.items():
            setattr(document, key, value)
        session.commit()
        session.refresh(document)
        return document
    raise HTTPException(status_code=404, detail="Document not found")
 

# Eliminar documento
@router.delete("/{document_id}")
def delete_document(document_id: int, session: session_dep):
    document = session.query(Document).filter(Document.id == document_id).first()
    if document:
        session.delete(document)
        session.commit()
        return {"detail": "Document deleted"}
    raise HTTPException(status_code=404, detail="Document not found")