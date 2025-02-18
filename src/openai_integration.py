import openai
import pandas as pd
from config import FILTERED_FILE, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_email(first_name, last_name, company):
    prompt = f"Write a professional sales email to {first_name} {last_name} at {company} introducing our product."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

def query_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def get_university_leads():
    df = pd.read_csv(FILTERED_FILE, encoding='latin1', low_memory=False)
    university_leads = df[df["Company"].str.contains("University", na=False)]
    
    return university_leads

if __name__ == "__main__":
    print(query_openai("List top 5 sales strategies for 2024"))
