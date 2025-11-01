from fastapi import FastAPI
from langgraph.types import Command
from fastapi.middleware.cors import CORSMiddleware
from app.routers.graph_router import router as graph_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI backend!"}

app.include_router(graph_router)