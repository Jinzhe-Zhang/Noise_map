from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
WIDTH=320
HEIGHT=240
RANGE=3
m=16
image = Image.open('pic.png')
image2 = Image.new('RGB',(320,240))
def color(tup):
    return tuple([sum(tup)//len(tup) for _ in tup])
for i in range(image.size[0]):
    for j in range(image.size[1]):
        image2.putpixel((i,j),color(image.getpixel((i,j))))
image2.save(open('newpic2.png','wb'),'png')