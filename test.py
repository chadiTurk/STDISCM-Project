# Image processing imports
import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageSequence
# Multiprocessing
import multiprocessing
# Operating system
import os, os.path
import time




def enhanceImage(brightnessFactor,sharpnessFactor,contrastFactor,image,folderLocation):

    
    openedImage = Image.open(image)
    imageFormat = openedImage.format

    if imageFormat == 'GIF' or 'gif':
        gifDuration = openedImage.info['duration']

        openedImage = ImageSequence.all_frames(
            openedImage, func=lambda frame: frame.convert("RGB"))

        openedImage = ImageSequence.all_frames(openedImage, func=lambda frame: 
        ImageEnhance.Brightness(frame).enhance(brightnessFactor))
        openedImage = ImageSequence.all_frames(openedImage, func=lambda frame: 
        ImageEnhance.Sharpness(frame).enhance(sharpnessFactor))
        openedImage = ImageSequence.all_frames(openedImage, func=lambda frame: 
        ImageEnhance.Contrast(frame).enhance(contrastFactor))

        openedImage[0].save(os.path.join(folderLocation, image),
                            save_all=True, append_images=openedImage[1:], duration=gifDuration, loop=0)
    
    else:

        openedImage = ImageEnhance.Brightness(openedImage)
        openedImage = openedImage.enhance(brightnessFactor)

        #brightenedImage.show()

        openedImage = ImageEnhance.Sharpness(openedImage)
        openedImage = openedImage.enhance(sharpnessFactor)

        #sharpenedImage.show()

        openedImage = ImageEnhance.Contrast(openedImage)
        openedImage = openedImage.enhance(contrastFactor)

        #contrastedImage.save(f"{folderLocation}/{contrastedImage.filename}.{contrastedImage.format}")
        print(imageFormat)
        
        #contrastedImage.show()
        openedImage.save(os.path.join(folderLocation, image))


if __name__ == "__main__":

    folderLocationUnenhanced = input("Folder location of images:")
    folderLocationEnhanced = input("Folder location of enhanced images:")
    enhancingTime = float(input("Enhancing time in minutes:"))
    brightnessFactor = float(input("Brightness enhancement factor:"))
    sharpnessFactor = float(input("Sharpness enhancement factor:"))
    contrastFactor = float(input("Contrast enhancement factor:"))

    os.chmod(folderLocationUnenhanced, 755)

    images = []
    #validImagesFormat = [".jpg",".gif",".png"]
    validImagesFormat = ['.gif']
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

