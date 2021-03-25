from PIL import Image
import pytesseract

img = Image.open("../Screenshots/pj.png")

text = pytesseract.image_to_string(img)

print(text)