# All this first part was cut from main.py

import json
import uuid                      # Used to generate Universally Unique Identifiers to prevent data collisions
from datetime import datetime    # Handles date and time generation
from pathlib import Path         # Provides an object-oriented approach to file system paths


def save_results_to_json(results: list[dict], filename: str = "results.json") -> None:       # Persists analysis results to a JSON file, maintaining history by appending to existing data. 
    path = Path(filename)                                                                    # Convert string to a Path object to utilize .exists() and other utilities
   
   # Check if the file already exists to avoid overwriting previous history
    if path.exists():                                            # if file exists, load existing data
        try:
            with open(path, "r", encoding="utf-8") as file:      # 'with' acts as a Context Manager: it ensures the file closes properly even if an error occurs
                existing_data = json.load(file)                  # "r" is reading mode  || encoding="utf-8" allows special characters || as file: is the temporary name for the open file. 
                                                                 # Load existing JSON content into a Python list
       
        except json.JSONDecodeError:  # Fallback: if the file is corrupted or empty, initialize a fresh list
            existing_data = []    

    else:                             # Initialize a new list if no previous file is found                  
        existing_data = []            # if the file doesn't exists it starts with an empty file.




    # Prepare new results by adding metadata (ID and Timestamp)

    enriched_results = []                                           # An empty list for new results. 

    for result in results:
        enriched_result = {
            "id": str(uuid.uuid4()),                                # Generate a unique string ID for database-like tracking
            "timestamp": datetime.now().astimezone().isoformat(),   # Generate timestamp in ISO 8601 format (standard for data exchange)
            **result                                                # '**' is Dictionary Unpacking: it copies all key-value pairs from 'result' into this new dict
        }



        enriched_results.append(enriched_result)

    # Merge historical data with the newly processed records
    combined_data = existing_data + enriched_results




    # Write the updated dataset back to the physical file

    with open(path, "w", encoding="utf-8") as file:                  
        json.dump(combined_data, file, indent=4, ensure_ascii=False)


        # "w" writing mode.
        # 'indent=4' makes the JSON file human-readable
        # 'ensure_ascii=False' ensures non-English characters (like accents) are saved correctly