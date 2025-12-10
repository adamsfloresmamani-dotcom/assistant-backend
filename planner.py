import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def plan_day(request_text):
    prompt = f"""
    Actúa como un asistente personal.
    Organiza y reprograma el día según este pedido:
    "{request_text}"

    Reglas:
    - Si hay imprevistos, reacomoda el día.
    - Si falta tiempo, elimina actividades de baja prioridad.
    - Responde en un texto corto con el plan del día.
    """

    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return result.choices[0].message["content"]
