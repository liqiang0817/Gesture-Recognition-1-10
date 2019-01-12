import cv2
import os

for classes in os.listdir('./val'):
    classpath = './val/' + classes
    for imgname in os.listdir(classpath):
        if not os.path.exists('./val224/' + classes):
            os.makedirs('./val224/' + classes)
        savepath = './val224/' + classes + '/' + imgname
        imgpath = classpath + '/' + imgname
        img = cv2.imread(imgpath) 
        img224 = cv2.resize(img, (224,224))
        cv2.imwrite(savepath, img224)
