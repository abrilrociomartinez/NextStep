email_text = "Unfortunately, we decided not to move forward with you application"

rejection_keywords = ["Unfortunately", "not to move forward"]


def email_classifier (rejection_keywords):
    if word in email_text:
        return "Rejection"

result = email_classifier(
    rejection_text,
    rejection_keywords, 
    mooving_forward_keywords,
    neutral_keywords
)

print(result)
