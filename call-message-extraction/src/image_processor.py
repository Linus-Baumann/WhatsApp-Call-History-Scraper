import os
from src.text_extractor import extract_text_from_image, extract_date_from_image
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
            
            date = extract_date_from_image(image_path)
            text = extract_text_from_image(image_path)
            call_messages = parse_call_messages(text, date)
            
            results.extend(call_messages)
    return results
