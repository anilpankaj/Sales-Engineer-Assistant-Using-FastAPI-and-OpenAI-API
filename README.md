# Sales Engineer Assistant - FastAPI and OpenAI API Project

## Overview
This project is a **Sales Engineer Assistant** built using **FastAPI** and **OpenAI API**. It automates lead processing, filtering, and email communication using OpenAI APIs. The assistant consolidates datasets, builds queries, and interacts with leads effectively.

## Features
- **Data Consolidation**: Merges multiple lead datasets into a structured format.
- **Lead Filtering**: Extracts relevant leads based on predefined criteria.
- **Sales Email Automation**: Generates personalized emails using OpenAI API.
- **FastAPI Backend**: Provides API endpoints for seamless integration.
- **OpenAI Assistant Integration**: Uses OpenAI APIs for intelligent responses.

## Project Structure
```
│── 📂 data/
│   ├── Leads.csv
│   ├── SampleData.csv
│── 📂 output/                 # Stores processed CSV files
│   ├── consolidated_leads.csv
│   ├── filtered_leads.csv
│── 📂 src/
│   ├── data_processing.py      # Handles data transformation and consolidation
│   ├── __init__.py             # <--- Add this empty file
│   ├── query_builder.py        # Builds queries based on lead data
│   ├── sdr_assistant.py        # Interacts with OpenAI API for email generation
│   ├── openai_integration.py   # FastAPI routes and endpoints
│── config.py
│── 📜 main.py
│── 📜 Dockerfile 
│── 📜 requirements.txt
│── 📜 README.md
```

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/sales-engineer-assistant.git
   cd sales-engineer-assistant
   ```
2. **Create a virtual environment**:
   ```sh
   python -m venv myenv
   source myenv/bin/activate   # For macOS/Linux
   myenv\Scripts\activate      # For Windows
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## How It Works
### 1. Data Processing (`data_processor.py`)
- Reads raw lead data from CSV files.
- Cleans and merges datasets into `consolidated_leads.csv`.
- Outputs processed data in `output/` directory.

### 2. Query Building (`query_builder.py`)
- Reads `consolidated_leads.csv`.
- Filters relevant leads based on conditions.
- Saves output as `filtered_leads.csv`.

### 3. Sales Email Generation (`sdr_assistant.py`)
- Reads `filtered_leads.csv`.
- Uses OpenAI API to generate personalized emails.
- Automates sales outreach.

### 4. FastAPI Integration (`api.py`)
- Provides RESTful API endpoints for lead processing and email generation.
- Accessible via `http://127.0.0.1:8000/docs`.

## Running the Project
1. **Run the main script**:
   ```sh
   python main.py
   ```
   - This will process data, filter leads, and send emails.

2. **Run the FastAPI Server**:
   ```sh
   uvicorn main:app --reload
   ```
   - Open API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Check if API is running |
| `POST` | `/process-leads` | Trigger lead processing |
| `POST` | `/send-emails` | Send emails to filtered leads |


## Future Enhancements
- Add more AI-driven insights for lead prioritization.
- Integrate CRM for lead tracking.
- Improve query optimization for better lead targeting.

---
🔥 **Start automating your sales process today!** 🚀

