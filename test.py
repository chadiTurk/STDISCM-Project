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
from itertools import repeat

def enhanceImage(image, folderLocationEnhanced, brightnessFactor,sharpnessFactor,contrastFactor):

    openedImage = Image.open(image)
    imageFormat = openedImage.format

    print("Image name: " + image + " saved")

    print('folderLocationEnhanced : ' + folderLocationEnhanced)

    if imageFormat == 'GIF':
        gifDuration = openedImage.info['duration']

        openedImage = ImageSequence.all_frames(
            openedImage, func=lambda frame: frame.convert("RGB"))

        openedImage = ImageSequence.all_frames(openedImage, func=lambda frame: 
        ImageEnhance.Brightness(frame).enhance(brightnessFactor))
        openedImage = ImageSequence.all_frames(openedImage, func=lambda frame: 
        ImageEnhance.Sharpness(frame).enhance(sharpnessFactor))
        openedImage = ImageSequence.all_frames(openedImage, func=lambda frame: 
        ImageEnhance.Contrast(frame).enhance(contrastFactor))

        openedImage[0].save(os.path.join(folderLocationEnhanced, image),
                            save_all=True, append_images=openedImage[1:], duration=gifDuration, loop=0)
    
    else:

        openedImage = ImageEnhance.Brightness(openedImage)
        openedImage = openedImage.enhance(brightnessFactor)

        openedImage = ImageEnhance.Sharpness(openedImage)
        openedImage = openedImage.enhance(sharpnessFactor)

        openedImage = ImageEnhance.Contrast(openedImage)
        openedImage = openedImage.enhance(contrastFactor)

        openedImage.save(os.path.join(folderLocationEnhanced, image))

def main():

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

    
    print("Number of images to process: " + str(len(images)))

    start_time = time.time()

    #With Multiprocessing

    pool = multiprocessing.Pool()
            
    pool.starmap(enhanceImage,zip(images,repeat(folderLocationEnhanced)
    ,repeat(brightnessFactor),repeat(sharpnessFactor),repeat(contrastFactor)))

    pool.close()

    pool.join()

    # With no multiprocessing

    # for image in images:
    #     enhanceImage(image,folderLocationEnhanced,brightnessFactor,sharpnessFactor,contrastFactor)

    st = os.listdir(folderLocationEnhanced)
    numberFiles = len(st)

    fileNameWithFolderName = os.path.join(folderLocationEnhanced,'statistics.txt')

    file = open(fileNameWithFolderName,"w")
    file.write('Number of images enhanced: ' + str(numberFiles) + '\n')
    file.write('Folder location: ' + folderLocationEnhanced)
    file.write('\n' + 'Processing time: ' + str(format(time.time() - start_time)))

    print('Processing time standard: {0} [sec]'.format(time.time() - start_time))

if __name__ == "__main__":
    main()
    

