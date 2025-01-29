import json
import os

def save_results(results):
    """
    Saves the analysis results to a JSON file.

    Args:
        results (dict): A dictionary containing the analysis results.
        output_path (str): File path to store results.

    Returns:
        None
    """
    output_path = "data/output/analysis_results.json"
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write results to JSON file
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print(f"Results saved successfully at: {output_path}")
