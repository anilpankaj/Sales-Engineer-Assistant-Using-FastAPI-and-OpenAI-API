import pandas as pd
from src.openai_integration import generate_email


FILTERED_FILE = r"E:\Kobe2.0\sales_engineer_project\output\filtered_leads.csv"


def send_sales_emails():
    df = pd.read_csv(FILTERED_FILE, encoding='latin1', low_memory=False)

    for index, row in df.iterrows():
        email_content = generate_email(row["First Name"], row["Last Name"], row["Company"])
        print(f"Email for {row['First Name']} {row['Last Name']}:\n{email_content}\n")

if __name__ == "__main__":
    send_sales_emails()
