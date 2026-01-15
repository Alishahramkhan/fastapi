from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# create fast api application
app = FastAPI()

# Enable CORS [Cross Origin Resource Sharing]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a request model
class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

# endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Corrected POST endpoint
@app.post("/chat")
async def asksomething(request: ChatRequest):
    print(f"Received query: {request.query}")
    query = request.query
    if query == 'how are you?':
        answer = "Thank you for asking I am fine"
    elif query == "what is your name?":
        answer = "My name is chatbot and i am not a terrorist"
    return ChatResponse(response=answer)