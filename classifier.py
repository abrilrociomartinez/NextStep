# La función de detectección y decisión 
# detect_signals | decide_status

# Contenido del email

email_text = email_text = "Thank you again for your application for the Administrative Assistant role. We were genuinely impressed with your profile on LinkedIn and are excited to potentially move forward with your candidacy. To help us move forward with your candidacy, please reply to this email with the following information: CV/Resume: A current, detailed resume in English (a profile photo is also requested). Salary Expectations: Your desired salary or compensation range."


# Las listas

rejection_keywords = ["unfortunately", 
                      "not to move forward", 
                      "desafortunadamente", 
                      "no seguir con tu proceso de selección", 
                      "have moved forward", "other candidates", 
                      "continue seeking", 
                      "pero agradecemos", 
                      "no", 
                      "hemos decidido no seguir con tu proceso de selección", 
                      "more closely align with", 
                      "encorauge", 
                      "better match"]

moving_forward_keywords = ["time sensitive", 
                           "next steps on your application", 
                           "Onboarding", 
                           "still missing", 
                           "requirements", 
                           "please", 
                           "complete", 
                           "still interested", 
                           "moving forward", 
                           "test", 
                           "as soon as possible", 
                           "48 hs", 
                           "48h", 
                           "48 h", 
                           "48hs",
                           "24hs", 
                           "24 hs", 
                           "24 h", 
                           "24h", 
                           "job description", 
                           "link", 
                           "important", 
                           "results", 
                           "reply", 
                           "confirm", 
                           "confirmation", 
                           "confirmación", 
                           "entrevista técnica", 
                           "entrevista", 
                           "técnica", 
                           "interview", 
                           "reunion", 
                           "reunión", 
                           "call", 
                           "llamada", 
                           "horarios", 
                           "group", 
                           "grupal", 
                           "individual", 
                           "next step", 
                           "siguiente paso", 
                           "propuesta", 
                           "próximos pasos", 
                           "equipo", 
                           "tareas", 
                           "tasks", 
                           "task", 
                           "within", 
                           "salary", 
                           "USD", 
                           "ARS", 
                           "próximo paso", 
                           "próximo", 
                           "hs", 
                           "h", 
                           "teams", 
                           "Teams", 
                           "encuentro", 
                           "minutos", 
                           "minutos", 
                           "brief", 
                           "Google Meets", 
                           "te esperamos"]

neutral_keywords = ["participar en la conversación", 
                    "artículo", 
                    "submitted successfully", 
                    "we wanted to share with you some of our latest job opportunities", 
                    "Ahora sigue estos pasos para llegar aún más lejos", 
                    "descubre empleos similares", 
                    "verify your", 
                    "account", 
                    "Se ha enviado tu solicitud a"]



# Defino la función de detección

def detect_signals(
        email_text,
        rejection_keywords,
        moving_forward_keywords,
        neutral_keywords
):
    email_text = email_text.lower()

    found = {
        "rejection" : [],
        "moving_forward": [],
        "neutral": []
    }

    for word in rejection_keywords:
        if word in email_text:
            found["rejection"].append(word)


    for word in moving_forward_keywords:
        if word in email_text:
            found["moving_forward"].append(word)

    for word in neutral_keywords:
        if word in email_text:
            found["neutral"].append(word)

    return found 

# Defino la función de decisión

def decide_status(signals):
    if signals["rejection"]:
        return "Rejection"

    if signals["moving_forward"]:
        return "Moving forward"
    
    if signals["neutral"]:
        return "Neutral"
    
    return "Unknown"

signals = detect_signals(
    email_text,
    rejection_keywords,
    moving_forward_keywords,
    neutral_keywords
)
status = decide_status(signals)

rejection_count = len(signals["rejection"])
moving_forward_count = len(signals["moving_forward"])
neutral_count = len(signals["neutral"])


print(signals)

# Para contar la cantidad de señales "Si al contar las señales del diccionario "rejection" dan un número mayor que cero, imprime la cantidad de señales.
if len(signals["rejection"]) > 0:
    print("Rejection signals detected:", rejection_count)

if len(signals["moving_forward"]) > 0:
    print("Moving forward signals detected:", moving_forward_count)

if len(signals["neutral"]) > 0:
    print("Neutral signals detected:", neutral_count)

print(status)

