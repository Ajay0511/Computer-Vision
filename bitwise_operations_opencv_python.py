import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = np.full((250, 500, 3), 255, dtype=np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)

print(img1.shape)

print(img2.shape)
bitand = cv2.bitwise_and(img2,img1)
bitor = cv2.bitwise_or(img2,img1)
bitXor = cv2.bitwise_xor(img2,img1)
bitnot = cv2.bitwise_not(img2)
bitnot1 = cv2.bitwise_not(img1)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('bit_and',bitand)
cv2.imshow('bit_or',bitor)
cv2.imshow('bit_xor',bitXor)
cv2.imshow('bitnot',bitnot)
cv2.imshow('bitnot1',bitnot1)
cv2.waitKey(0)
cv2.destroyAllWindows()