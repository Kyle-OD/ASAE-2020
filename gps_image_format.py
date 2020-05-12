import PIL
from PIL import Image

img_name = "airfield_test.JPG"

width = 670
height = 400
img = Image.open(img_name)
img = img.resize((width, height), PIL.Image.ANTIALIAS)
img.save('formatted_' + img_name)
