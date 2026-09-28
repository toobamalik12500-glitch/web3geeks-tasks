from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import google.generativeai as genai
import os
import requests

app = FastAPI()

# --- Config ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FISH_API_KEY = os.getenv("FISH_API_KEY")
FISH_MODEL_ID = os.getenv("FISH_MODEL_ID") # Railway Variables me ye bhi add karna

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

AUDIO_PATH = "/tmp/last_audio.mp3"

class ChatRequest(BaseModel):
    message: str
    history: list = []

# --- Voice Generate Function (SDK ke bagair) ---
def make_voice(text):
    try:
        url = "https://api.fish.audio/v1/tts"
        headers = {
            "Authorization": f"Bearer {FISH_API_KEY}",
            "Content-Type": "application/json"
        }
        # Fish ka naya payload format
        data = {
            "text": text,
            "reference_id": FISH_MODEL_ID,
            "format": "mp3",
            "mp3_bitrate": 128
        }
        resp = requests.post(url, json=data, headers=headers, timeout=30)
        print("Fish Status:", resp.status_code)
        if resp.status_code == 200:
            with open(AUDIO_PATH, "wb") as f:
                f.write(resp.content)
            return True
        else:
            print("Fish Error:", resp.text)
            return False
    except Exception as e:
        print("Voice Exception:", e)
        return False

@app.post("/voice")
def voice_chat(req: ChatRequest):
    # 1. Gemini se jawab lo
    prompt = f"You are a real estate agent. Reply in short Urdulish. User: {req.message}"
    gemini_resp = model.generate_content(prompt)
    reply_text = gemini_resp.text.strip()

    # 2. Usi jawab ki voice banao
    success = make_voice(reply_text)
    
    if not success:
        return JSONResponse({"reply_urdulish": reply_text, "error_voice": "Fish API failed, check API Key / Model ID / Balance"})

    return {"reply_urdulish": reply_text, "audio_ready": True}

@app.get("/audio")
def get_audio():
    if not os.path.exists(AUDIO_PATH):
        return JSONResponse({"error": "No audio file yet, call /voice first"}, status_code=404)
    return FileResponse(AUDIO_PATH, media_type="audio/mpeg", filename="voice.mp3")

@app.get("/")
def home():
    return {"status": "ok"}
