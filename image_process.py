import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

def find_num(im):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray , (5,5), 0)
    edge = cv2.Canny(blurred, 50, 200, 255)
    th3 = cv2.adaptiveThreshold(edge,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2)
    dil = cv2.dilate(th3, np.ones((2, 2), np.uint8), iterations=1)
    
    #plt.imshow(edge)
    
    digitCnts = []
    arr=[]
    cnts = cv2.findContours(dil.copy(),1,2)
    maxi = -1
    h=im.shape[0]
    w=im.shape[1]
    bbox = ( w//4, h//4 , w//2 , h//2 ) ## default in case no bbox is found
    for c in cnts[1]:
        (x, y, w, h) = cv2.boundingRect(c)
#        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        arr.append((w,h))
        if w>50 and w<300 and h>50 and h<500 and w*h>maxi:
            maxi = w*h
            bbox = (x,y,w,h)
#            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    x=bbox[0]-50
    y=bbox[1]-50
    w=bbox[2]+100
    h=bbox[3]+100
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
#    cv2.imshow('default',im)
#    cv2.waitKey(0)
    return (im, bbox)

def crop(im, bbox):
    x=max(bbox[0]-20,0)
    y=max(bbox[1]-20,0)
    w=min(bbox[2]+40,im.shape[1]-1)
    h=min(bbox[3]+40,im.shape[0]-1)
    crop_img = im[ y:y+h, x:x+w ]
#    print(y,x,y+h,x+w)
#    print("crop img",crop_img.shape)
    crop_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    crop_blur = cv2.GaussianBlur(crop_gray , (13,13), 0)
    
    th = cv2.adaptiveThreshold(crop_blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2)
    res = cv2.resize(th,(28,28))
#    plt.imshow(res, cmap="gray")
    return res
    
#im = cv2.imread('n6.jpg')
#marked_img, bbox = find_num(im)
#number_img = crop(im, bbox)
#img = np.reshape(number_img, (1,28,28,1))
