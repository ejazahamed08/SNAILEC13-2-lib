import pytesseract
from PIL import Image

img = Image.open('receipt.png')

text = pytesseract.image_to_string(img)

print(text)