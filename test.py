# Image processing imports
import PIL
from PIL import Image
from PIL import ImageEnhance
# Multiprocessing
import multiprocessing


def enhanceImage(brightnessFactor,sharpnessFactor,contrastFactor,image):

    currentBrightness = ImageEnhance.Brightness(image)
    brightenedImage = currentBrightness.enhance(brightnessFactor)

    brightenedImage.show()

    currentSharpness = ImageEnhance.Sharpness(brightenedImage)
    sharpenedImage = currentSharpness.enhance(sharpnessFactor)

    sharpenedImage.show()

    currentContrast = ImageEnhance.Contrast(sharpenedImage)
    contrastedImage = currentContrast.enhance(contrastFactor)

    contrastedImage.show()



if __name__ == "__main__":
    image_variable_name = Image.open("test.jpg")
    enhanceImage(1,100,50,image_variable_name)