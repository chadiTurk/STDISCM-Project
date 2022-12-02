# Image processing imports
import PIL
from PIL import Image
from PIL import ImageEnhance
# Multiprocessing
import multiprocessing
# Operating system
import os, os.path
import time




def enhanceImage(brightnessFactor,sharpnessFactor,contrastFactor,image,folderLocation):

    
    openedImage = Image.open(image)
    imageFormat = openedImage.format
    
    currentBrightness = ImageEnhance.Brightness(openedImage)
    brightenedImage = currentBrightness.enhance(brightnessFactor)

    #brightenedImage.show()

    currentSharpness = ImageEnhance.Sharpness(brightenedImage)
    sharpenedImage = currentSharpness.enhance(sharpnessFactor)

    #sharpenedImage.show()

    currentContrast = ImageEnhance.Contrast(sharpenedImage)
    contrastedImage = currentContrast.enhance(contrastFactor)

    #contrastedImage.save(f"{folderLocation}/{contrastedImage.filename}.{contrastedImage.format}")
    print(imageFormat)
    contrastedImage.save(os.path.join(folderLocation, image))
    #contrastedImage.show()



if __name__ == "__main__":

    folderLocationUnenhanced = input("Folder location of images:")
    folderLocationEnhanced = input("Folder location of enhanced images:")
    enhancingTime = float(input("Enhancing time in minutes:"))
    brightnessFactor = float(input("Brightness enhancement factor:"))
    sharpnessFactor = float(input("Sharpness enhancement factor:"))
    contrastFactor = float(input("Contrast enhancement factor:"))

    os.chmod(folderLocationUnenhanced, 755)

    images = []
    validImagesFormat = [".jpg",".gif",".png"]

    for files in os.listdir(folderLocationUnenhanced):
        checkFileFormat = os.path.splitext(files)[1]
        if checkFileFormat.lower() not in validImagesFormat:
            continue
        images.append((os.path.join(folderLocationUnenhanced,files)))
  
    numberOfProcesses = multiprocessing.cpu_count()
    print(numberOfProcesses)

    start_time = time.time()

    for image in images:
        enhanceImage(brightnessFactor,sharpnessFactor,contrastFactor,image,folderLocationEnhanced)
    
    print('Processing time standard: {0} [sec]'.format(time.time() - start_time))

