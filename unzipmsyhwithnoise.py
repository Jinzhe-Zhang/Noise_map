import pytesseract
from PIL import Image
image=Image.open('picmsyh.png')
r,g,b=image.split()
image=r.point(lambda x:255-x)
image.save(open('picwhitemsyh.png','wb'),"png")
image.show()
pytesseract.pytesseract.tesseract_cmd = r'D:\OCR\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image,lang='chi_sim')
d=open("结果\\resultmsyhwithnoise.txt","w")
d.write(text)
d.close()
print(text)