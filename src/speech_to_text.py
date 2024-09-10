import asyncio
import websockets
import json
import os
from dotenv import load_dotenv

load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
DEEPGRAM_URL = f"wss://api.deepgram.com/v1/listen?encoding=linear16&sample_rate=16000&channels=1&model=nova-2"

async def speech_to_text(audio_chunk):
    async with websockets.connect(DEEPGRAM_URL, extra_headers={"Authorization": f"Token {DEEPGRAM_API_KEY}"}) as ws:
        await ws.send(audio_chunk)
        response = await ws.recv()
        result = json.loads(response)
        if result.get("is_final"):
            transcript = result["channel"]["alternatives"][0]["transcript"]
            return transcript
