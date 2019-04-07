from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
WIDTH=320
HEIGHT=240
RANGE=1
m=16
def color(i,j,rangee):
    ary=[]
    for ii in range(i-rangee,i+rangee+1):
        for jj in range(j-rangee,j+rangee+1):
            if 0<=ii<WIDTH and 0<=jj<HEIGHT:
                ary.append((ii,jj))
    return ary
def avg(a):
    b=[0 for _ in range(len(a[0]))]
    for i in a:
        for j in range(len(i)):
            b[j]+=i[j]
    for i in range(len(b)):
        b[i]//=len(a)
    #return tuple(b)
    if sum(b)>384:
        return tuple(255 for _ in range(len(b)))
    else:
        return tuple(0 for _ in range(len(b)))
image = Image.open('picmsyh.png')
image2 = Image.new('RGB',(320,240))
for i in range(image.size[0]):
    for j in range(image.size[1]):
        image2.putpixel((i,j),avg(list(map(lambda x:image.getpixel(x),color(i,j,RANGE)))))
image2.save(open('newpic.png','wb'),'png')