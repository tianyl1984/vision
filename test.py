image="C:\\Users\\tianyl\\Downloads\\vision\\source_1.png"
from PIL import Image

im = Image.open(image)
width = 120
height = 30
x = 760
y = 1300
box = (x, y, x + width, y + height)
region = im.crop(box)
region.show()
