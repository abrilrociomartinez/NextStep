# Import keyword sets for signal detection from the local configuration
from keywords import (
    REJECTION_KEYWORDS,
    MOVING_FORWARD_KEYWORDS,
    NEUTRAL_KEYWORDS
)

# Import the core logic for email processing
from classifier import detect_signals, decide_status
from persistence import save_results_to_json

def analyze_email(email_text: str) -> dict:
# Analizes a single email string and returns a structured classification object. 

     # Parameters (args): 
     #              email_text (str): The raw text content of the email
    
     # Returns:
     #               dict: A dictionary containing:
     #                  - email_text (str) the original text
     #                  - status (str) the final status
     #                  - signals (dict) the specific keyword signals detected
    
    
     # Execute keyword detection by comparing email text against predefined lists
    signals = detect_signals(
        email_text=email_text,
        rejection_keywords=REJECTION_KEYWORDS,
        moving_forward_keywords=MOVING_FORWARD_KEYWORDS, 
        neutral_keywords=NEUTRAL_KEYWORDS
    )

    # Apply priority logic to determine the final category (e.g., 'Rejected', 'Interview')
    status = decide_status(signals)

    #  Construct the final data structure (avoiding side effects like 'print' here)
    return {
        "email_text": email_text,    # Original email content
        "status": status,            # Final Classification
        "signals": signals           # Detected keyword signals
    }




def analyze_batch(emails: list[str]) -> list[dict]:
    # Processes a list of email strings and aggregates their individual analysis results.

        # Parameters:   
        #               emails (list[str]): A collection of email body strings.

        # Returns:
        #               list[dict]: A list of result dictionaries.

    results: list[dict] = []  # Storage for processed email data

    for email_text in emails:
        # Process each individual email using the analyze_email function.
        result = analyze_email(email_text)
        # Append the result dictionary to the results list.
        results.append(result)

    # Return all processed results.
    return results










# Main Execution Block

if __name__ == "__main__":
 # Define a sample dataset for testing the classification logic
    sample_emails = [
        "Thank you for your application, we would like to invite you to an interview",
        "Unfortunately, we decided to move forward with other candidates",
        "Your application has been submitted successfully"
    ]
    # Process the sample batch
    results = analyze_batch(sample_emails)
   
    # Save findings to the local filesystem
    save_results_to_json(results)
    print("\nResults saved to results.json")
    
    
    # Display formatted output in the console for verification
    for result in results:
        # Print results for each analyzed email.
        print("-" * 40)
        print(f"Status: {result['status']}")
        print(f"Signals: {result['signals']}")