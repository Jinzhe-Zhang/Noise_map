import pytesseract
from PIL import Image
image=Image.open('timg.jpg')
pytesseract.pytesseract.tesseract_cmd = r'D:\OCR\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image,lang='chi_sim')
d=open("结果\\articleresult.txt","w")
d.write(text)
d.close()
print(text)