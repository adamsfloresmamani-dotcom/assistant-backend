from flask import Flask, request, jsonify
from stt import transcribe
from tts import speak
from planner import plan_day
import base64
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post("/server")
def server():

    if "audio" not in request.files:
        return jsonify({"error": "No se envió audio"}), 400

    file = request.files["audio"]

    audio_bytes = file.read()

    text = transcribe(audio_bytes)
    plan = plan_day(text)
    voice_mp3 = speak(plan)

    return jsonify({
        "plan": plan,
        "voice": base64.b64encode(voice_mp3).decode()
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
