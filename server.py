from flask import Flask, request, jsonify, send_from_directory
from stt import transcribe
from tts import speak
from planner import plan_day
import base64
import os

app = Flask(__name__, static_url_path='', static_folder='.')

@app.post("/server")
def server():
    if "audio" not in request.files:
        return jsonify({"error": "No se envió audio"}), 400

    audio = request.files["audio"]

    text = transcribe(audio)
    plan = plan_day(text)
    voice_mp3 = speak(plan)

    return jsonify({
        "plan": plan,
        "voice": base64.b64encode(voice_mp3).decode()
    })

@app.get("/")
def index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
