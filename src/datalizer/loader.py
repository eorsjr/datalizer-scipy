import os
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load a dataset from a file into a pandas DataFrame.
    
    Supported formats: .csv, .xlsx, .json

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the file extension is unsupported or reading fails.
        
    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    elif file_path.endswith(".json"):
        return pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}. Please use .csv, .xlsx, or .json.")