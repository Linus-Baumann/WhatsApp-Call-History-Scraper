from src.image_processor import process_screenshots

def main():
    screenshot_dir = './data/input/'
    call_data = process_screenshots(screenshot_dir)
    
    for call in call_data:
        print(f"Date: {call['date']}, Type: {call['type']}, Duration: {call['duration']}")

if __name__ == "__main__":
    main()
