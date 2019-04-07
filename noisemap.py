from PIL import Image
import random
image = Image.new('RGB',(320,240))
for i in range(image.size[0]):
    for j in range(image.size[1]):
        image.putpixel((i,j),(random.randint(0,256),random.randint(0,256),random.randint(0,256)))
image.save(open('noisemap.png','wb'),'png')