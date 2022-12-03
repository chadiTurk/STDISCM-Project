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
import sys


folderLocationUnenhanced = ''
folderLocationEnhanced = './enhancedImages'
enhancingTime = 1
brightnessFactor = 1
sharpnessFactor = 1
contrastFactor = 1


def enhanceImage(image):

    

    openedImage = Image.open(image)
    imageFormat = openedImage.format

    print("Image name: " + image + " saved")

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

        #brightenedImage.show()

        openedImage = ImageEnhance.Sharpness(openedImage)
        openedImage = openedImage.enhance(sharpnessFactor)

        #sharpenedImage.show()

        openedImage = ImageEnhance.Contrast(openedImage)
        openedImage = openedImage.enhance(contrastFactor)

        #contrastedImage.save(f"{folderLocation}/{contrastedImage.filename}.{contrastedImage.format}")

        
        #contrastedImage.show()

        openedImage.save(os.path.join(folderLocationEnhanced, image))


if __name__ == "__main__":

    # folderLocationUnenhanced,folderLocationEnhanced,enhancingTime
    # brightnessFactor, sharpnessFactor, contrastFactor

    #lock = multiprocessing.Lock()

    
    #sys.stdin = open(0)

    folderLocationUnenhanced = input("Folder location of images:")
    
    folderLocationEnhanced = input("Folder location of enhanced images:")
    
    enhancingTime = float(input("Enhancing time in minutes:"))
    brightnessFactor = float(input("Brightness enhancement factor:"))
    sharpnessFactor = float(input("Sharpness enhancement factor:"))
    contrastFactor = float(input("Contrast enhancement factor:"))


    os.chmod(folderLocationUnenhanced, 755)

    images = []
    validImagesFormat = [".jpg",".gif",".png"]
    #validImagesFormat = ['.gif']
    for files in os.listdir(folderLocationUnenhanced):
        checkFileFormat = os.path.splitext(files)[1]
        if checkFileFormat.lower() not in validImagesFormat:
            continue
        images.append((os.path.join(folderLocationUnenhanced,files)))
  
    
    print("Number of images to process: " + str(len(images)))

    start_time = time.time()

    # sharedManager = multiprocessing.Manager()

    # sharedImages = sharedManager.list(images)
    # sharedLock = sharedManager.Semaphore(1)
    


    
    pool = multiprocessing.Pool()
            
    pool.map(enhanceImage,images)

    pool.close()


    #pool.join()

    # for image in images:
    #     enhanceImage(image)

    st = os.listdir(folderLocationEnhanced) # your directory path
    numberFiles = len(st)

    fileNameWithFolderName = os.path.join(folderLocationEnhanced,'statistics.txt')

    file = open(fileNameWithFolderName,"w")
    file.write('Number of images enhanced: ' + str(numberFiles) + '\n')
    file.write('Folder location: ' + folderLocationEnhanced)


    # with open(os.path.join(folderLocationEnhanced,"copied_text_file.txt", '+w')) as text:
    #     text.write(numberFiles)
    #     text.write(folderLocationUnenhanced)

    
    print('Processing time standard: {0} [sec]'.format(time.time() - start_time))

