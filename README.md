# NextStep - Modular Email Classification Pipeline

## Overview

NextStep is a modular email classification pipeline built in Python. 
It analyzes recruitment-related emails and categorizes them into:

- Moving Forward
- Rejection
- Neutral 


The project is designed following clean architecture principles and structured as a scalable data-processing system. 

---


## Architecture 

The project follows separation of concerns:

- 'classifier.py' → Core business logic (signal detection & status decision)
- 'persistence.py' → Data storage layer (JSON handling, ID generation, timestamps)
- 'main.py' → Orchestration layer
- 'results.json' → Structured output storage


This modular design allows future expansion (database, APIs, analytics).


---


## Currect Features 

- Keyword-based email classification
- Batch email processing
- Structured JSON persistance
- Unique ID generation (UUID4)
- ISO 8601 timestamp tracking (timezone-aware)
- Corrupted JSON handling
- Modular architecture (clean separation of responsabilities)


---


## Example Output Structure

Each processed  email is stored as:


```json
{
  "id": "uuid",
  "timestamp": "ISO8601",
  "email_text": "original email",
  "status": "Moving forward / Rejection / Neutral",
  "signals": {
      "rejection": [],
      "moving_forward": [],
      "neutral": []
  }
}

```
---


## Tech Stack


- Python 3.10+
- JSON
- Standard Library (uuid, datetime, pathlib)


---


## Roadmap

- Regex-based word boundary matching
- Pandas analytics layer
- CSV export
- Database integration
- Gmail API ingestion


---


## Author 

Abril Rocío Martínez
Law Student | Data Engineering Apprenticegit push