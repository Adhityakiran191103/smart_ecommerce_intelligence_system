"""Main project entry point.

This will be connected to the completed modules near the end of the project.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.ecommerce_intelligence.data_loader import load_retail_data


def main():
    df = load_retail_data()
    print("Dataset loaded successfully.")
    print(f"Rows: {len(df):,}")
    print("Columns:", list(df.columns))
    print("\nNext: connect cleaning, analysis, RFM, segmentation and reporting modules.")


if __name__ == "__main__":
    main()
