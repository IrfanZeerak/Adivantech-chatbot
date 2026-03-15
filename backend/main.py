from fastapi import FastAPI
from pydantic import BaseModel
from backend.chatbot import get_response
app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):

    reply = get_response(msg.message)

    return {"response": reply}