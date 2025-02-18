import pandas as pd

def filter_leads():
    file_path = "E:\\Kobe2.0\\sales_engineer_project\\output\\consolidated_leads.csv"
    df = pd.read_csv(file_path, encoding="latin1")

    # Debugging: Print column names
    print("Columns in DataFrame:", df.columns.tolist())
    

    # Identify the correct column
    lead_origin_col = "Lead Origin_x" if "Lead Origin_x" in df.columns else "Lead Origin_y"

    # Handle case where neither exists
    if lead_origin_col not in df.columns:
        raise KeyError("Neither 'Lead Origin_x' nor 'Lead Origin_y' found in DataFrame.")

    # Filter data
    filtered_df = df[(df[lead_origin_col] == "Landing Page Submission") & 
                     (df["Company"].notna() | df["Mobile Number"].notna() | df["LinkedIn URL"].notna())]

    output_path = "E:\\Kobe2.0\\sales_engineer_project\\output\\filtered_leads.csv"
    filtered_df.to_csv(output_path, index=False)

    print(f"Filtered leads saved to {output_path}")
