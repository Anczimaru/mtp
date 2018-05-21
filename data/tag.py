
import numpy
import cv2
import os.path
import matplotlib.pyplot as plt
import  PIL
from PIL import Image

face_detect_count=0
cascade_path = 'haarcascade_frontalface_alt.xml'
image_count=460
for i in range(image_count):
    if os.path.isfile('zack\image(' + str(i) + ')'+ '.jpeg'):
        image_path = ('zack\image('+ str(i)+').jpeg')
        color = (255, 0, 0) #blue
        #reading file 
        image = cv2.imread(image_path)
        #change to gray scale
        image_gray =cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        #obtaining cascade 
        cascade = cv2.CascadeClassifier(cascade_path)
        #face recognition
        facerect = cascade.detectMultiScale(
                        image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
        
        # image synthesis
       
        layer1 = Image.open( image_path )
        layer2 = Image.open( 'sholip.png' )
        # change to RGBA mode for image synthesis
        layer1 = layer1.convert('RGBA')
        # prepare same size campus
        c = Image.new('RGBA', layer1.size, (255, 255,255, 0))
        # rect[0]:x, rect[1]:y, rect[2]:width, rect[3]:height

        for rect in facerect:
            # resize our sholip logo
            resize_img = layer2#layer2.resize((rect[2], rect[3]))
            # overwrite to the campus 
            c.paste(resize_img, (rect[0],rect[1]), resize_img)
        # combine original one and campus and save
        result = Image.alpha_composite(layer1, c)
        result.save('cut_zack\image('+ str(face_detect_count)+').png')
        face_detect_count= face_detect_count + 1
    else:
      print('image' + str(i) + ':No File')
