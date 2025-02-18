import os

BASE_DIR = "E:\\Kobe2.0\\sales_engineer_project"

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

LEADS_FILE = os.path.join(DATA_DIR, "Leads.csv")
SAMPLE_DATA_FILE = os.path.join(DATA_DIR, "SampleData.csv")

CONSOLIDATED_FILE = os.path.join(OUTPUT_DIR, "consolidated_leads.csv")
FILTERED_FILE = os.path.join(OUTPUT_DIR, "filtered_leads.csv")

OPENAI_API_KEY = "YOUR-OPENAI-API-KEY"
