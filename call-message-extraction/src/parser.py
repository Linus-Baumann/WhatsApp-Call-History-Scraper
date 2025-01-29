import math
import re

CALL_PATTERN = re.compile(r'(Videoanruf|Sprachanruf)', re.IGNORECASE)
DURATION_PATTERN = re.compile(r'(\d+ Std\. \d+ Min\.)')

def parse_call_messages(image, messages):
    """
    Parse call messages and durations from OCR text.
    Includes date from the extracted grey box.
    """
    call_messages = []
    
    for message in messages:
        cleaned_content = str(message['content']).replace(",", ".").replace(";", ".")  # Handle OCR variations
        cleaned_content = cleaned_content.replace("Std", "Std.").replace("Min", "Min.")  # Ensure uniform format

        hour_match = re.search(r"(\d+)\s*Std\.?", cleaned_content)
        minute_match = re.search(r"(\d+)\s*Min\.?", cleaned_content)
        second_match = re.search(r"(\d+)\s*Sek\.?", cleaned_content)
        # Check if "Min" is present; otherwise, raise an error
        if not minute_match and not second_match:
            continue

        # Extract hours (optional)
        hours = int(hour_match.group(1)) if hour_match else 0

        # Extract minutes (required)
        minutes = int(minute_match.group(1)) if minute_match else 0

        # Extract seconds (optional, only present if no hours)
        seconds = int(second_match.group(1)) if second_match else 0

        call_messages.append({
            'type': message['type'],
            'duration': (hours * 60) + minutes + math.ceil(seconds / 60)
        })
    
    return call_messages
