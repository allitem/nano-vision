from PIL import Image
import pytesseract

def read_image(path):
    return pytesseract.image_to_string(Image.open(path))
