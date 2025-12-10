from flask import Flask, request, jsonify
from stt import transcribe
from tts import speak
from planner import plan_day
import base64
import os

app = Flask(__name__)

@app.post("/server")
def server():
    # 🟢 Validar si llegó un archivo
    if "audio" not in request.files:
        return jsonify({"error": "No se envió audio"}), 400

    audio = request.files["audio"]

    # 🟢 Conversión de voz a texto
    text = transcribe(audio)

    # 🟢 Planificador IA
    plan = plan_day(text)

    # 🟢 Conversión del plan a voz
    voice_mp3 = speak(plan)

    # 🟢 Retornar MP3 en base64 (para usar en el celular)
    return jsonify({
        "plan": plan,
        "voice": base64.b64encode(voice_mp3).decode()
    })

if __name__ == "__main__":
    # Render necesita host=0.0.0.0 y puerto dinámico
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
