import re

CALL_PATTERN = re.compile(r'(Videoanruf|Sprachanruf)', re.IGNORECASE)
DURATION_PATTERN = re.compile(r'(\d+ Std\. \d+ Min\.)')

def parse_call_messages(text, date):
    """
    Parse call messages and durations from OCR text.
    Includes date from the extracted grey box.
    """
    call_messages = []
    lines = text.split('\n')
    
    for line in lines:
        call_type_match = CALL_PATTERN.search(line)
        duration_match = DURATION_PATTERN.search(line)
        
        if call_type_match:
            call_type = call_type_match.group(1)
            call_duration = duration_match.group(1) if duration_match else None
            
            call_messages.append({
                'type': call_type,
                'duration': call_duration,
                'date': date
            })
    
    return call_messages
