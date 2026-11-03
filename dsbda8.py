import json
import pandas as pd

# Load JSON file
with open("data.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print("JSON DATASET ANALYSIS")
print("=" * 40)
print("JSON file loaded successfully: data.json")
print("Total records:", len(df))
print("Key fields:", ", ".join(df.columns))

# Basic Analysis
print("\nBASIC ANALYSIS")
print("Average Age:", round(df["age"].mean(), 2))
print("Average Salary:", round(df["salary"].mean(), 2))

# Department-wise Employee Count
print("\nDEPARTMENT-WISE EMPLOYEE COUNT")
print(df["department"].value_counts().to_string())

# Gender Distribution
print("\nGENDER DISTRIBUTION")
print(df["gender"].value_counts().to_string())

# Age Group Analysis
print("\nAGE GROUP ANALYSIS")
bins = [float("-inf"), 19, 30, 40, 50, float("inf")]
labels = ["< 20", "20 - 30", "31 - 40", "41 - 50", "> 50"]

df["Age Group"] = pd.cut(df["age"], bins=bins, labels=labels)
print(df["Age Group"].value_counts(sort=False).to_string())

# Display First Five Records
print("\nSAMPLE RECORDS (first 5)")
print(df.drop(columns=["Age Group"]).head().to_string(index=False))

print("\nAnalysis completed successfully!")