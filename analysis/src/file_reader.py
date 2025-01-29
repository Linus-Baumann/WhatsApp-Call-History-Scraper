import csv
import os

def read_calls_from_csv():
    """
    Reads the call history CSV file and returns a list of call records.
    
    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        list[dict]: List of dictionaries containing call records.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    csv_path = "data/input/call_records.csv"
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Convert to list of dictionaries
