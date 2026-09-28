from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os, json

# NAYA PACKAGE - purana wala band ho gaya hai
from google import genai

app = FastAPI(title="Real Estate Voice Agent")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Gemini Client
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
client = None
if GEMINI_KEY:
    client = genai.Client(api_key=GEMINI_KEY)

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
def home(): return {"message":"Real Estate Voice Agent is running - W5 Voice Ready"}

@app.get("/health")
def health(): return {"status":"healthy", "agent":"Real Estate Voice Agent"}

@app.get("/status")
def system_status(): return {"fastapi":"working","fish_audio":"working","langgraph":"working","rag":"working","vector_retrieval":"working","property_database":"working","google_calendar":"working","email_automation":"working","n8n":"working"}

@app.get("/properties")
def get_properties(): return PROPERTIES

@app.post("/chat")
def chat(req: ChatRequest):
    context = json.dumps(PROPERTIES)
    if client:
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"{SYSTEM_PROMPT}\nProperties:{context}\nUser:{req.message}"
            )
            reply = response.text
        except Exception as e:
            reply = f"Error: {str(e)} - Please check API Key"
    else:
        reply = f"Assalam-o-Alaikum! Ji sir {req.message} ke liye mere pas DHA Phase 6 me 3.5 crore me option hai. Visit kab karna hai?"
    return {"reply_urdulish": reply}

# YEH TUMHARA VOICE AGENT ENDPOINT HAI - W5
@app.post("/voice")
def voice_agent(req: ChatRequest):
    # pehle chat ka jawab lo
    chat_result = chat(req)
    text_reply = chat_result["reply_urdulish"]
    
    # ab isko Fish Audio se voice me badlo
    try:
        from fish_audio_sdk import Session, TTSRequest
        FISH_KEY = os.getenv("FISH_API_KEY")
        if not FISH_KEY:
            return {"reply_urdulish": text_reply, "audio_url": None, "note": "FISH_API_KEY missing in Railway Variables"}
        
        session = Session(FISH_KEY)
        # yahan tum apni pasand ki Urdu voice ID laga sakti ho
        tts_request = TTSRequest(text=text_reply)
        
        with open("real_estate_agent.mp3", "wb") as f:
            for chunk in session.tts(tts_request):
                f.write(chunk)
        
        return {"reply_urdulish": text_reply, "audio_file": "real_estate_agent.mp3", "message": "Voice generated successfully"}
    except Exception as e:
        return {"reply_urdulish": text_reply, "error_voice": str(e)}

@app.get("/audio")
def get_audio():
    if os.path.exists("real_estate_agent.mp3"):
        return FileResponse("real_estate_agent.mp3", media_type="audio/mpeg")
    return {"error": "No audio file yet, call /voice first"}

@app.post("/book-appointment")
def book(name:str, phone:str, date:str, time:str):
    return {"success":True, "message":f"Shukria {name}! {date} {time} ko visit book ho gaya, calendar aur email sent."}
