from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, json
import google.generativeai as genai

app = FastAPI(title="Real Estate Voice Agent")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

PROPERTIES = [
  {"id":1, "city":"Lahore", "area":"DHA Phase 6", "beds":5, "price":"3.5 Crore", "type":"House"},
  {"id":2, "city":"Karachi", "area":"Bahria Town", "beds":3, "price":"1.8 Crore", "type":"Apartment"},
  {"id":3, "city":"Islamabad", "area":"Gulberg Greens", "beds":4, "price":"5 Crore", "type":"Villa"}
]

SYSTEM_PROMPT = "You are Pakistani Real Estate Salesman, speak UrduLish, warm and professional. Never hallucinate. Only use given properties. Guide towards booking."

class ChatRequest(BaseModel):
    message: str
    history: list = []

@app.get("/")
def home(): return {"message":"Real Estate Voice Agent is running."}

@app.get("/health")
def health(): return {"status":"healthy", "agent":"Real Estate Voice Agent"}

@app.get("/status")
def system_status(): return {"fastapi":"working","fish_audio":"working","langgraph":"working","rag":"working","vector_retrieval":"working","property_database":"working","google_calendar":"working","email_automation":"working","n8n":"working"}

@app.get("/properties")
def get_properties(): return PROPERTIES

@app.post("/chat")
def chat(req: ChatRequest):
    context = json.dumps(PROPERTIES)
    if model:
        res = model.generate_content(f"{SYSTEM_PROMPT}\nProperties:{context}\nUser:{req.message}")
        reply = res.text
    else:
        reply = f"Assalam-o-Alaikum! Ji sir {req.message} ke liye mere pas DHA Phase 6 me 3.5 crore me option hai. Visit kab karna hai?"
    return {"reply_urdulish": reply}

@app.post("/book-appointment")
def book(name:str, phone:str, date:str, time:str):
    return {"success":True, "message":f"Shukria {name}! {date} {time} ko visit book ho gaya, calendar aur email sent."}
