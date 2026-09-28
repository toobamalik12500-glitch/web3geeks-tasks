from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from google import genai
import os
import requests
import traceback

app = FastAPI()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FISH_API_KEY = os.getenv("FISH_API_KEY")
FISH_MODEL_ID = os.getenv("FISH_MODEL_ID")

client = genai.Client(api_key=GEMINI_API_KEY)

AUDIO_PATH = "/tmp/last_audio.mp3"

class ChatRequest(BaseModel):
    message: str
    history: list = []

def make_voice(text):
    url = "https://api.fish.audio/v1/tts"
    headers = {"Authorization": f"Bearer {FISH_API_KEY}"}
    data = {"text": text, "reference_id": FISH_MODEL_ID, "format": "mp3"}
    resp = requests.post(url, json=data, headers=headers, timeout=40)
    print(f"Fish {resp.status_code}: {resp.text[:500]}")
    if resp.status_code == 200:
        with open(AUDIO_PATH, "wb") as f:
            f.write(resp.content)
        return True, ""
    return False, resp.text

@app.post("/voice")
def voice_chat(req: ChatRequest):
    try:
        if not GEMINI_API_KEY or not FISH_API_KEY or not FISH_MODEL_ID:
            return JSONResponse({"error": "Keys missing", "gemini": bool(GEMINI_API_KEY), "fish": bool(FISH_API_KEY), "model": bool(FISH_MODEL_ID)}, status_code=500)

        # NEW GEMINI MODEL
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Reply in short Urdulish (roman urdu + english mix) as a Pakistani real estate agent. Keep it under 2 lines. User: {req.message}"
        )
        reply_text = response.text.strip()

        ok, err = make_voice(reply_text)
        if not ok:
            return {"reply_urdulish": reply_text, "error_voice": err, "audio_ready": False}

        return {"reply_urdulish": reply_text, "audio_ready": True}
    except Exception as e:
        traceback.print_exc()
        return JSONResponse({"error": str(e), "trace": traceback.format_exc()}, status_code=500)

@app.get("/audio")
def get_audio():
    if not os.path.exists(AUDIO_PATH):
        return JSONResponse({"error": "No audio yet"}, status_code=404)
    return FileResponse(AUDIO_PATH, media_type="audio/mpeg")

@app.get("/")
def home():
    return {"status": "ok new gemini 2.0"}
