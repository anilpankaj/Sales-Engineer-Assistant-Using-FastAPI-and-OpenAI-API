import pandas as pd
from config import LEADS_FILE, SAMPLE_DATA_FILE, CONSOLIDATED_FILE

def load_data():
    # Read CSV files
    leads_df = pd.read_csv(LEADS_FILE, encoding='latin1', low_memory=False)
    sample_df = pd.read_csv(SAMPLE_DATA_FILE, encoding='latin1', low_memory=False)

    return leads_df, sample_df

def consolidate_data():
    leads_df, sample_df = load_data()

    # Merge based on 'Prospect ID' (assuming it's a common key)
    merged_df = pd.merge(leads_df, sample_df, on="Prospect ID", how="outer")

    # Save to CSV
    merged_df.to_csv(CONSOLIDATED_FILE, index=False)
    print(f"Consolidated data saved to {CONSOLIDATED_FILE}")

if __name__ == "__main__":
    consolidate_data()
