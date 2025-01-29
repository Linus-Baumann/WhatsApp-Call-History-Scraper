from PIL import Image
import pytesseract as tesseract

# Configure Tesseract executable path
tesseract.pytesseract.tesseract_cmd = r'E:\Programme\Tesseract\tesseract.exe'

def extract_call_messages_from_image(image, messages):
    """
    Extract full text from the given regions using OCR.
    :return: A list of extracted call messages with the format: ((x, y, width, height), Video, Content)
    """
    call_messages = []

    for message in messages:
        cropped_image = image[message['region'][1]:message['region'][1] + message['region'][3], message['region'][0]:message['region'][0] + message['region'][2]]
        text = tesseract.image_to_string(cropped_image, lang='deu', config="--psm 7")
        call_messages.append({
            'region': message['region'],
            'type': message['type'],
            'content': text
        })
        print("Extracted text:", text)
    return call_messages

def extract_dates_from_image(image):
    """
    Extract the dates from the small grey boxes in the image.
    Assumes the dates are located at two-thirds of the image width.
    Returns the extracted date as a string with the bottom coordinate of the box.
    """
    width, height = image.size
    
    # Crop region containing the date
    crop_box = (width * 2 // 3, 0, width, height // 8)
    date_image = image.crop(crop_box)
    return tesseract.image_to_string(date_image, lang='deu').strip()
