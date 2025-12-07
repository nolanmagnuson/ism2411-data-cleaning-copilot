data_cleaning.py

Purpose:
    This script loads a messy sales dataset, applies a series of cleaning steps,
    and outputs a clean CSV file. It demonstrates standard data cleaning practices
    including column normalization, whitespace stripping, handling missing values,
    and removing invalid rows.

"""

import pandas as pd


# -----------------------------------------------------------
# Function: load_data
# What it should do:
#   Load a CSV file into a pandas DataFrame.
# Why:
#   Keeps loading logic modular and testable.
# NOTE:
#   Copilot generated the initial version of this function.
#   I kept the structure but simplified unnecessary arguments.
# -----------------------------------------------------------
def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


# -----------------------------------------------------------
# Function: clean_column_names
# What it should do:
#   Lowercase, strip whitespace, replace spaces/hyphens with underscores.
# Why:
#   Standard naming prevents errors when selecting or merging columns.
# NOTE:
#   Copilot suggested a more complex regex approach; I simplified it.
# -----------------------------------------------------------
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


# -----------------------------------------------------------
# Function: handle_missing_values
# What it should do:
#   Remove rows missing essential values: price OR quantity.
#   Strip whitespace from product/category fields.
# Why:
#   Sales entries without these fields cannot be analyzed.
# NOTE:
#   Copilot initially proposed filling missing values with 0.
#   I changed the logic to drop rows instead.
# -----------------------------------------------------------
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Strip whitespace from text columns
    if "prodname" in df.columns:
        df["prodname"] = df["prodname"].astype(str).strip().str.strip()
    if "category" in df.columns:
        df["category"] = df["category"].astype(str).str.strip()

    # Drop rows missing critical numeric values
    df = df.dropna(subset=["price", "qty"])

    return df


# -----------------------------------------------------------
# Function: remove_invalid_rows
# What it should do:
#   Remove rows with negative price or quantity.
# Why:
#   Negative values are clearly data-entry errors.
# NOTE:
#   Copilot suggested using abs() to convert negatives to positives.
#   I replaced that with stricter filtering logic.
# -----------------------------------------------------------
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df


# -----------------------------------------------------------
# MAIN EXECUTION PIPELINE
# -----------------------------------------------------------
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
