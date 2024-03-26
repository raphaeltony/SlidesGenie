from pytesseract import pytesseract
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
TESSERACTPATH = os.getenv("TESSERACT_PATH")  

def get_text(FILEPATH):
    img = Image.open(FILEPATH)
    pytesseract.tesseract_cmd = TESSERACTPATH
    text = pytesseract.image_to_string(img)
    print("Extracted text : ", text)
    return text


# print(get_text('../new.png'))
