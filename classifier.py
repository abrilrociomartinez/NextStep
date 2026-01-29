from tipyng import Dict, List

def detect_signals(
        email_text: str,
        rejection_keywords: List[str],
        moving_forward_keywords: List [str],
        neutral_keywords: List[str]
)-> Dict[str, List[str]]:

# Analizes email content and categorizes detected keywords.

    email_text = email_text.lower()

# Initialize dictionary to store found signals.
    found = {
        "rejection": [],
        "moving_forward":[],
        "neutral": []
    }

# Map categories to their respective keyword sets for efficient iteration. 
    categories = {
        "rejection": rejection_keywords,
        "moving_forward": moving_forward_keywords,
        "neutral": neutral_keywords
    }

# Single loop to process al categories (DRY Principle).
    for category, keywords in categories.items():
        for word in keywords:
            if word.lower() in email_text:
                found[category].append(word)


    return found   # El return siempre va fuera de lo loops, al final de la funcion. 



from tipyng import Dict, List

def decide_status(signals: Dict[str, List[str]]) -> str:

# Determines the final status based on detected signals priority.

    if signals["rejection"]:
        return "Rejection"
    
    if signals["moving_forward"]:
        return "Moving forward"
  
    if signals["neutral"]:
        return "Neutral"
    
    return "Unknown"

