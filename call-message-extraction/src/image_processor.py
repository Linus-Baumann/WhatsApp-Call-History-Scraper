import os
import cv2
from src.text_extractor import extract_dates_from_image
from src.screen_analysis import extract_call_message_regions_from_image
from src.parser import parse_call_messages

def process_screenshots(screenshot_dir):
    """
    Process all screenshots to extract and parse call messages.
    """
    results = []
    for filename in sorted(os.listdir(screenshot_dir)):
        if filename.endswith('.png') or filename.endswith('.png'):
            image_path = os.path.join(screenshot_dir, filename)
            print(f"Processing: {image_path}")
            image = cv2.imread(image_path)
            
            dates = extract_dates_from_image(image)
            call_message_regions = extract_call_message_regions_from_image(image)
            call_messages = extract_call_messages_from_image(image, call_message_regions)
            call_details = parse_call_messages(call_messages, dates)
            
            results.extend(call_details)
    return results
