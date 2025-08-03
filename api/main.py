
from fastapi import FastAPI
from api.routers.UserRouter import router as UserRouter
from api.routers.DocumentRouter import router as DocumentRouter

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

app.include_router(UserRouter, prefix="/users", tags=["users"])
app.include_router(DocumentRouter, prefix="/documents", tags=["documents"])

@app.on_event("startup")
def startup_event():
    from api.db.database import create_database_and_tables
    create_database_and_tables()
    print("Database and tables created on startup.")

