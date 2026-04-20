
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="Doubt Wale API")

PERSONAS = {
    "kabir": {
        "name": "Kabir",
        "voice_style": "warm, wise, simple",
        "prompts": {
            "hi": "Tum Kabir ho. Class {grade} NCERT Maths ko 3 steps mein bahut simple Hindi mein samjhao. Roz ki zindagi ka example do. Sirf Maths. End: 'Samajh aaya?'",
            "en": "You are Kabir. Explain Class {grade} NCERT Maths in 3 simple steps in clear English. Use a daily-life example. Maths only. End: 'Did that make sense?'"
        }
    },
    "ira": {
        "name": "Ira",
        "voice_style": "patient, encouraging",
        "prompts": {
            "hi": "Tum Ira ho. Class {grade} NCERT Maths ko 3 steps mein aasan Hindi mein samjhao. Example do. Sirf Maths. End: 'Samajh aaya?'",
            "en": "You are Ira. Explain Class {grade} NCERT Maths in 3 simple steps in English. Use an everyday example. Maths only. End: 'Did that make sense?'"
        }
    }
}

FIRST_TIME_MSG = {
    "hi": "Doubt Wale mein swagat! Pehle bhasha chuno: 1 for Hindi, 2 for English. Phir tutor chuno: Kabir ya Ira.",
    "en": "Welcome to Doubt Wale! First choose language: 1 for Hindi, 2 for English. Then pick tutor: Kabir or Ira."
}

@app.get("/")
def health():
    return {"product": "Doubt Wale", "classes": [5,6,7,8], "subject": "Maths", "personas": list(PERSONAS.keys())}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    # Expected payload from WhatsApp: user_id, text, image_url, is_first_time
    is_first = data.get("is_first_time", False)
    if is_first:
        # send language choice
        return JSONResponse({"message": FIRST_TIME_MSG["hi"] + " | " + FIRST_TIME_MSG["en"]})

    persona = data.get("persona", "kabir")  # kabir or ira
    lang = data.get("lang", "hi")  # hi or en
    grade = int(data.get("grade", 6))

    prompt = PERSONAS[persona]["prompts"][lang].format(grade=grade)
    # TODO: call vision model with prompt + image
    return JSONResponse({
        "persona": persona,
        "lang": lang,
        "grade": grade,
        "prompt_used": prompt,
        "status": "ready_for_vision"
    })
