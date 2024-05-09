import pytesseract as tess
tess.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image
path="static\download.png"

image=Image.open(path)
text=tess.image_to_string(image,lang="hin")
text=text.strip()
text=text.lower()
print(text)

from translate import Translator
try:
    translator= Translator(from_lang="hindi",to_lang="english")
    text = translator.translate(text)
    print(text)
except Exception as e:
    pass


# from pypdf import PdfReader 
# inp="english"
# out="spanish"
# reader = PdfReader(path) 
# l=len(reader.pages) 
# tex=""
# for i in range(l):
#     page = reader.pages[i] 
#     text = page.extract_text() 
#     text.strip()
#     print(text)
#     if inp!="input language" and out!="output language":
#         try:
#             translator= Translator(from_lang=inp,to_lang=out)
#             tex = translator.translate(text[100:450])
#         except Exception as e:
#             print(e)
#     print(tex)