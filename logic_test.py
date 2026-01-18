rejection_text = "Unfortunately, we decided not to move forward with your application"
moving_forward_text = "Thank you again for your application for the Administrative Assistant role. We were genuinely impressed with your profile on LinkedIn and are excited to potentially move forward with your candidacy. To help us move forward with your candidacy, please reply to this email with the following information: CV/Resume: A current, detailed resume in English (a profile photo is also requested). Salary Expectations: Your desired salary or compensation range."
neutral_text = "Lee este artículo en LinkedIn para participar en la conversación"


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

for word in rejection_keywords:
    if word in rejection_text.lower():
        print("Rechazo detectado:", word)

for word in moving_forward_keywords:
    if word in moving_forward_text.lower():
        print("Avance en el proceso:", word)

for word in neutral_keywords:
    if word in neutral_text.lower():
        print("Correo neutro:", word)
