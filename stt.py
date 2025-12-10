import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe(audio_file):
    result = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return result.text
