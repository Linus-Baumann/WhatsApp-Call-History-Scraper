import csv
import os

def write_calls_to_csv(data):
    """
    Writes a list of call records to a CSV file, ensuring the directory exists.
    If the file exists, it will be overwritten unless overwrite=False.

    Args:
        data (list of dicts): A list of dictionaries, each containing 'type' and 'duration'.
        output_file (str): The file path where the CSV will be saved.
        overwrite (bool): Whether to overwrite the file if it exists (default: True).

    Returns:
        None

    Raises:
        ValueError: If the data list is empty.
        IOError: If the file cannot be written.
    """
    output_file='./data/output/call_records.csv'
    overwrite=True

    # Ensure the data is not empty
    if not data:
        raise ValueError("The data list is empty. Nothing to write to CSV.")

    # Ensure the directory exists
    directory = os.path.dirname(output_file)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)  # Create directory if it doesn't exist
        except OSError as e:
            raise IOError(f"Failed to create directory {directory}: {e}")

    # Check if file exists and handle overwrite option
    if os.path.exists(output_file):
        if not overwrite:
            raise IOError(f"File '{output_file}' already exists and overwrite is disabled.")
        else:
            print(f"Overwriting existing file: {output_file}")

    # Get field names from the first dictionary (assumes all entries have the same keys)
    fieldnames = data[0].keys()

    # Write the CSV file (overwrites by default)
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write column names
            writer.writerows(data)  # Write the list of dictionaries

        print(f"CSV file saved successfully at: {output_file}")
    
    except IOError as e:
        raise IOError(f"Error writing to file {output_file}: {e}")

