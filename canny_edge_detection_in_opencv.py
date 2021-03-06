import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg',0)
canny = cv2.Canny(img,100,200)

titles = ['image','Canny']
images = [img,canny]
for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()