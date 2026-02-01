# Import keyword lists used to detect signals in the email text.
from keywords import (
    moving_forward_keywords,
    rejection_keywords,
    neutral_keywords
)

# Import core classification logic functions.
from classifier import detect_signals, decide_status

def analize_email(test_email: str) -> dict:
# Analizes a single email and returns structured results. 


    # Call the classifier to detect keyword-based signals.

    signals = detect_signals(
        email_text=test_email,
        rejection_keywords=rejection_keywords,
        moving_forward_keywords=moving_forward_keywords, 
        neutral_keywords=neutral_keywords
    )

    # Decide the final status based on detected signals.
    status = decide_status(signals)

    # Return structured data instead of printing.
    return {
        "email": email_text,    # Original email content
        "status": status,       # Final Classification
        "signals": signals      # Detected keyword signals
    }

def analyze_batch(emails: list[str]) -> list[dict]:
    # Processes multiple emails and aggregates their analysis results.

    results = []  # Initialize empty list to store analysis outputs.

    for email in emails:
        # Analyze each email individually.
        result = analyze_email(email)
        # Append the result dictionary to the results list.
        results.append(result)

    # Return all processed results.
    return results

if __name__ == "__main__":
    # Entry point of the application (execution layer).

    emails = [
        "Thank you for your application, we would like to invite you to an interview",
        "Unfortunately, we decided to move forward with other candidates",
        "Your application has been submitted successfully"
    ]
    # Example batch of emails for testing.

    results = analyze_batch(emails)
    # Run batch analysis on all emails.

    for r in results:
        # Print results for each analyzed email.
        print("-" * 40)
        print(f"Status: {r['status']}")
        print(f"Signals: {r['signals']}")