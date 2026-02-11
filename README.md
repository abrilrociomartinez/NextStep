# NextStep - English version

**NextStep** is a keyword-based email classification pipeline focused on recruitment process outcomes. It is designed as a modular data-processing system, with future plans for automation and integrations. Its goal is to filter incoming emails, detect deadlines for technical tests and interviews, and automatically organize the schedule to ensure no opportunity is missed.

## CurrentScope
- Keyword-based email classification
- Modular architecture (separation of concerns)
- Structured outputs for future persistance (JSON / CSV)
- Designed as a data processing pipeline

## Roadmap
- JSON and CSV persistance
- Deadline extraction (regex + datetime)
- Batch analysis with Pandas
- Gmail API intgration
- Database-ready schema
- **Libraries:** `imaplib`, `email`, `re` (Regex)


## Features (In Development)
- **Smart Filtering:** Distinguishes between rejections and next steps in selection processes using keyword analysis.
- **Deadline Detection:** Extracts dates and timeframes (e.g., "within 48 hours") to prioritize technical tests.
- **Gmail Integration:** Direct API connection to read, classify, and manage emails securely.

## Tech Stack
- **Language:** Python 3.10+


## Author
**Abril Rocío Martínez** - *Law Student | Data Engineering & Cybersecurity Apprentice*

# NextStep - Spanish version
**NextStep** es un asistente inteligente de automatización para procesos de reclutamiento. Su objetivo es filtrar correos electrónicos, detectar plazos de tests y entrevistas y organizar la agenda automáticamente.

## Funcionalidades (En desarrollo)
- **Filtro Inteligente:** Distingue entre rechazos y avances en procesos de selección usando palabras clave. 
- **Detección de Deadlines:** Extrae fechas (ej: "dentro de 48 horas") para que no se pase ninguna prueba técnica. 
- **Integración con Gmail:** Conexión directa vía API para leer y clasificar correos. 


## Tecnologías 
- **Lenguaje:** Python 3.10+
- **Librerías:** `imaplib`, `email`, `re` (Regex)

## Autora
**Abril Rocío Martínez** - *Law student | Data Engineering & Cybersecurity Apprentice*
