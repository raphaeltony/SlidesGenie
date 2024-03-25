from pytesseract import pytesseract
from PIL import Image

TESSERACTPATH = "D:/Apps/teseract/tesseract.exe"    

def get_text(FILEPATH):
    img = Image.open(FILEPATH)
    pytesseract.tesseract_cmd = TESSERACTPATH
    text = pytesseract.image_to_string(img)
    return text


print(get_text('../new.jpg'))
