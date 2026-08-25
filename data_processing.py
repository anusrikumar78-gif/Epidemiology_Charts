
import pandas as pd
import os


def load_data():

    # Find the main project folder
    base_path = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    # Find disease_data.csv inside data folder
    csv_path = os.path.join(
        base_path,
        "data",
        "disease_data.csv"
    )

    # Load CSV
    df = pd.read_csv(csv_path)

    # Convert numeric columns
    df["Year"] = pd.to_numeric(
        df["Year"],
        errors="coerce"
    )

    df["Cases"] = pd.to_numeric(
        df["Cases"],
        errors="coerce"
    )

    df["Deaths"] = pd.to_numeric(
        df["Deaths"],
        errors="coerce"
    )

    # Clean text columns
    df["Disease"] = (
        df["Disease"]
        .astype(str)
        .str.strip()
    )

    df["Gender"] = (
        df["Gender"]
        .astype(str)
        .str.strip()
    )

    df["Region"] = (
        df["Region"]
        .astype(str)
        .str.strip()
    )

    df["Age_Group"] = (
        df["Age_Group"]
        .astype(str)
        .str.strip()
    )

    # Remove rows where important numeric data is missing
    df = df.dropna(
        subset=[
            "Year",
            "Cases",
            "Deaths"
        ]
    )

    return df
