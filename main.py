from fastapi import FastAPI, Query
from pydantic import BaseModel
import pandas as pd
import openai
import os

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Load lead data (Modify path as needed)
df = pd.read_csv("output/filtered_leads.csv", encoding="latin1")

class LeadQuery(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Sales Engineer Assistant API is running!"}

# 1️⃣ **Query Leads with Natural Language**
@app.post("/query_leads/")
def query_leads(data: LeadQuery):
    user_input = data.query

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You analyze lead data and return SQL queries."},
                  {"role": "user", "content": f"Convert this into an SQL query: {user_input}"}]
    )

    sql_query = response["choices"][0]["message"]["content"]
    return {"sql_query": sql_query}

# 2️⃣ **Generate Personalized Sales Emails**
@app.get("/generate_email/")
def generate_email(first_name: str = Query("Valued Customer"), 
                   last_name: str = Query(""), 
                   company: str = Query("your company")):
    
    prompt = f"""
    Generate a personalized sales outreach email for {first_name} {last_name} at {company}. 
    Make it professional but engaging, mentioning how our solution can help their business.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a professional sales assistant."},
                  {"role": "user", "content": prompt}]
    )

    return {"email_content": response["choices"][0]["message"]["content"]}

# 3️⃣ **Retrieve Lead Data from CSV**
@app.get("/leads/")
def get_leads(country: str = None, min_score: int = 0):
    filtered_df = df[df["Lead Score"] >= min_score]
    if country:
        filtered_df = filtered_df[filtered_df["Country"] == country]

    return filtered_df.to_dict(orient="records")
