import PIL
from PIL import Image
from PIL import ImageEnhance

image_variable_name = Image.open("test.jpg")
image_variable_name.show()

curr_bri = ImageEnhance.Brightness(image_variable_name)
new_bri = 10

# Brightness enhanced by a factor of 2.5
img_brightened = curr_bri.enhance(new_bri)

# shows updated image in image viewer
img_brightened.show()
