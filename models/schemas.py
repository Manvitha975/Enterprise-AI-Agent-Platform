from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class ResearchRequest(BaseModel):
    question: str
class ResearchResponse(BaseModel):

    status: str
    agent: str
    question: str
    answer: str

class DocumentResponse(BaseModel):
    status: str
    agent: str
    summary: str