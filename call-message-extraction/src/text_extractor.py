from PIL import Image
import pytesseract as tesseract

# Configure Tesseract executable path
tesseract.pytesseract.tesseract_cmd = r'E:\Programme\Tesseract\tesseract.exe'

def extract_text_from_image(image_path):
    """
    Extract full text from an image using OCR.
    """
    image = Image.open(image_path)
    return tesseract.image_to_string(image, lang='deu')  # Use German language for OCR

def extract_date_from_image(image_path):
    """
    Extract the date from the small grey box in the image.
    Assumes the date is located at two-thirds of the image width and near the top.
    """
    image = Image.open(image_path)
    width, height = image.size
    
    # Crop region containing the date
    crop_box = (width * 2 // 3, 0, width, height // 8)
    date_image = image.crop(crop_box)
    return tesseract.image_to_string(date_image, lang='deu').strip()
