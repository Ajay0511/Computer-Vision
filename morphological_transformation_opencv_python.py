import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,225,cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)  #Erosion followed by dilation
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)


titles = ['image','mask','dilation','erosion','opening','closed']
images=[img,mask,dilation,erosion,opening,closing]

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()