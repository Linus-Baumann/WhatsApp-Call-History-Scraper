import os
import cv2
from src.parser import parse_call_messages
from src.debug_helper import mark_regions
from src.screen_analysis import extract_call_message_regions_from_image
from src.text_extractor import extract_call_messages_from_image, extract_dates_from_image
from src.file_writer import write_calls_to_csv

def main():
    screenshot_dir = './data/input/'
    results = []
    for filename in sorted(os.listdir(screenshot_dir)):
        if filename.endswith('.png') or filename.endswith('.png'):
            image_path = os.path.join(screenshot_dir, filename)
            print(f"Processing: {image_path}")
            image = cv2.imread(image_path)
            
            #dates = extract_dates_from_image(image)
            call_message_regions = extract_call_message_regions_from_image(image)
            call_messages = extract_call_messages_from_image(image, call_message_regions)
            call_details = parse_call_messages(image, call_messages)
            
            results.extend(call_details)
            write_calls_to_csv(results)


if __name__ == "__main__":
    main()
