import os
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel

def process():
    DIFF = 0.01

    # Image Path
    inputPath = "C:/"
    savingPath = "C:/Data/20230426/"


    countSaving = 0
    countReading = 0
    countEachCam = dict(Cam00=0, Cam01=0, Cam02=0, Cam03=0)
    files = {}
    prevImage = {}


    app = QApplication([])
    label = QLabel("Hello")
    label.show()

    app.exec()

    for x in os.walk(inputPath):
        if len(x[2]) != 0:
            directory = x[0][-5:]
            files[directory] = []
            for file in x[2]:
                files[directory].append(file)
            countReading += len(files[directory])
    





    for file in files:
        path = os.path.join(savingPath, file)
        if not os.path.exists(path):
            os.makedirs(path)


        for image in files[file]:
            prefix = image[:5]
            path = os.path.join(savingPath, file, prefix)

            if not os.path.exists(path):
                os.makedirs(path)
            
            match prefix:
                case "Cam00":
                    ## PARAMETER (CROP = 600 x 600)
                    ## CAMERA 0
                    left = 520
                    right = 1120
                    up = 310
                    down = 910

                    
                case "Cam01":
                    ## PARAMETER (CROP = 600 x 600)                    
                    ## CAMERA 1
                    left = 482
                    right = 1082
                    up = 295
                    down = 895


                case "Cam02":
                    ## PARAMETER (CROP = 600 x 600)                    
                    ## CAMERA 2
                    left = 430
                    right = 1030
                    up = 320
                    down = 920

                               
                case "Cam03":
                    ## PARAMETER (CROP = 600 x 600)                    
                    ## CAMERA 3
                    left = 435
                    right = 1035
                    up = 325
                    down = 925
            
                   
            os.chdir(path)
            imagePath = os.path.join(inputPath, file, image)
            img = cv2.imread(imagePath)
            crop = img[up:down, left:right]

            if prefix in prevImage:
                diffPercent = imageDifference(crop, prevImage[prefix])
                #print(diffPercent)
                if diffPercent < DIFF:
                    print("DUPLICATED IMAGE")
                else:
                    cv2.imwrite(image, crop)
                    countSaving += 1
                    countEachCam[prefix] += 1

            prevImage[prefix] = crop
            print("Each Cam: {} / Total Saving: {} / Total Reading : {}".format(countEachCam, countSaving, countReading))


    print("{}% Conversion Succeed".format((countSaving / countReading) * 100))


def imageDifference(img1, img2):
    diff = cv2.absdiff(img1, img2)
    diff = diff.astype(np.uint8)
    return (np.count_nonzero(diff)) / diff.size 

            


#TEST ONLY
def imageCrop():
    ## PARAMETER (CROP = 600 x 600)
    ## CAMERA 1
    left = 435
    right = 1035
    up = 325
    down = 925

    path = "C:/Users/howon/OneDrive/Desktop/Cam03_00040222_20230426 165653_941.jpg"
    path2 = "C:/Users/howon/OneDrive/Desktop/Cam02_00040241_20230426 165653_445.jpg"


    img = cv2.imread(path)
    img2 = cv2.imread(path2)
    
    diff = cv2.absdiff(img, img2)
    diff = diff.astype(np.uint8)
    print((np.count_nonzero(diff)) / diff.size) 

    #crop = img[up:down, left:right]
    #cv2.imshow('image', crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gui():
    app = QApplication([])
    label = QLabel("Hello")
    label.show()

    app.exec()




gui()
#imageCrop()