# Image processing imports
import PIL
from PIL import Image
from PIL import ImageEnhance
# Multiprocessing
import multiprocessing
# Operating system
import os, os.path




def enhanceImage(brightnessFactor,sharpnessFactor,contrastFactor,image):

    currentBrightness = ImageEnhance.Brightness(image)
    brightenedImage = currentBrightness.enhance(brightnessFactor)

    #brightenedImage.show()

    currentSharpness = ImageEnhance.Sharpness(brightenedImage)
    sharpenedImage = currentSharpness.enhance(sharpnessFactor)

    #sharpenedImage.show()

    currentContrast = ImageEnhance.Contrast(sharpenedImage)
    contrastedImage = currentContrast.enhance(contrastFactor)

    #contrastedImage.show()



if __name__ == "__main__":

    folderLocationUnenhanced = input("Folder location of images:")
    folderLocationEnhanced = input("Folder location of enhanced images:")
    enhancingTime = input("Enhancing time in minutes:")
    brightnessFactor = input("Brightness enhancement factor:")
    sharpnessFactor = input("Sharpness enhancement factor:")
    contrastFactor = input("Contrast enhancement factor:")

    images = []
    validImagesFormat = ['.jpg','.gif','.png']

    for files in os.listdir(folderLocationUnenhanced):
        checkFileFormat = os.path.splitext(files)[1]
        if checkFileFormat.lower() not in validImagesFormat:
            continue
        images.append(Image.open(os.path.join(folderLocationUnenhanced,files)))
    #image_variable_name = Image.open("test.jpg")
    #enhanceImage(1,100,50,image_variable_name)

    images[0].show()
    numberOfCores = multiprocessing.cpu_count()
    print(numberOfCores)

