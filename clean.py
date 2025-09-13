import pandas as pd

# Load the CSV
df = pd.read_csv("recording_export.csv")

def clean_cell(x):
    if isinstance(x, str):
        # Remove line breaks and extra spaces
        return " ".join(x.split())
    return x

# Apply cleaning to every cell
df = df.applymap(clean_cell)

# Save cleaned CSV
df.to_csv("recording_export_flat.csv", index=False, encoding="utf-8")

print("Saved cleaned CSV as recording_export_flat.csv")
