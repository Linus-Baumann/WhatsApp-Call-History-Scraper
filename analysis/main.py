from src.file_reader import read_calls_from_csv
from src.analyzer import calculate_total_duration
from src.file_writer import save_results

def main():    
    # Read data
    call_data = read_calls_from_csv()

    # Analyze data
    total_duration = calculate_total_duration(call_data)

    # Save results
    results = {"total_duration": total_duration}
    save_results(results)

    print(f"Total Call Duration: {total_duration} minutes")

if __name__ == "__main__":
    main()
