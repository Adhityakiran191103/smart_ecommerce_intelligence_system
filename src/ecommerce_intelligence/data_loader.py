"""Load the source retail dataset."""
import pandas as pd
from .config import DEFAULT_DATA_FILE


def load_retail_data(file_path=DEFAULT_DATA_FILE):
    """Load an Excel dataset and return a DataFrame."""
    file_path = str(file_path)
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Dataset not found: {file_path}. Put Online Retail.xlsx in data/raw/ "
            "or pass the correct file path."
        ) from exc
