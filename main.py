from keywords import (
    moving_forward_keywords,
    rejection_keywords,
    neutral_keywords
)
from classifier import detect_signals, decide_status

def run_analysis(test_email: str):
    # Orchestrates the email analysis process and prints formatted results.
    print(f"--- Analizing Email ---")


    # 1. Detect the signals

    signals = detect_signals(
        email_text=test_email,
        moving_forward_keywords=moving_forward_keywords, 
        rejection_keywords=rejection_keywords,
        neutral_keywords=neutral_keywords
    )

    # 2. Make a decision
    status = decide_status(signals)

    # 3. Show detailed results
    print(f"Fianl Result: {status}")
    print(f"Signals found: {signals}")
    print("-" * 20)

if __name__ == "__main__":
    # Here I can put a text in order to see if its working
    sample_text = "Thank you for your application, we would like to invite you to an interview"
    run_analysis(sample_text)