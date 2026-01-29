def detect_signals(email_text, rejection_keywords, moving_forward_keywords, neutral_keywords):

# Analizes email content and categorizes detected keywords.

    email_text = email_text.lower()

# Initialize dictionary to store found signals.
    found = {
        "moving_forward":[],
        "rejection": [],
        "neutral": []
}

# Map categories to their respective keyword sets for efficient iteration. 
    categories = {
        "moving_forward": moving_forward_keywords,
        "rejection": rejection_keywords, 
        "neutral": neutral_keywords
}

# Single loop to process al categories (DRY Principle).
    for category, keywords in categories.items():
        for word in keywords:
            if word.lower() in email_text:
                found[category].append(word)


    return found



def decide_status(signals: Dict:[str, List[str]]) -> str:

# Determines the final status based on detected signals priority.

    if signals["moving_forward"]:
        return "Moving forward"
   
    if signals["rejection"]:
        return "Rejection"
  
    if signals["neutral"]:
        return "Neutral"
    
    return "Unknown"

