import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

class Novel(BaseModel):
    name: str
    chapterCount: int

class Novels(BaseModel):
    novels: List[Novel]

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allowed_credentials=True,
    allowed_methods=["*"],
    allowed_headers=["*"],
)

memory_db = {"novels": []}

@app.get(path="/novels", response_model=Novels)
def get_novel():
    return Novels(novels=memory_db["novels"])

@app.post(path="/novels", response_model=Novel)
def add_novel(novel: Novel):
    memory_db["novels"].append(novel)
    return novel

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)