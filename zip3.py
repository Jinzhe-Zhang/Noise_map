from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
m=16
image = Image.new('RGB',(320,240))
font = ImageFont.truetype('msyh.ttc',48)
draw = ImageDraw.Draw(image)
draw.text((60, 100),"你能看清\n  我吗？",(255,255,255),font=font)
image.save(open('fontmsyh.jpg','wb'),'jpeg')
for i in range(image.size[0]):
    for j in range(image.size[1]):
        image.putpixel((i,j),(random.randint(0,256-m)+image.getpixel((i,j))[0]*m//256,random.randint(0,256-m)+image.getpixel((i,j))[1]*m//256,random.randint(0,256-m)+image.getpixel((i,j))[2]*m//256))
image.save(open('picmsyh.png','wb'),'png')