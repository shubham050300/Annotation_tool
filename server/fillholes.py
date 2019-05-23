import numpy as np
import cv2

from collections import Counter



xrange = range


imgor = cv2.imread("1.jpg", 1);

img = imgor[:, :, 2]
# img[img==255] = 1


imgclose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=None)
imgbin = cv2.threshold(imgclose, 200, 255, cv2.THRESH_BINARY)[1]

ret, labels = cv2.connectedComponents(imgbin)

cv2.imshow('Closed image', imgbin) 
  
cv2.waitKey(0) 


for i in range(1, ret+1):
	xpoints = (labels==i).nonzero()[0]
	ypoints = (labels==i).nonzero()[1]

	if(xpoints.shape[0] < 10):
		# print("here")
		for j in xrange(xpoints.shape[0]):
			imgbin[xpoints[j]][ypoints[j]] = 0


ret, labels = cv2.connectedComponents(imgbin)


# imgbin is the final binary image ie 0 or 255
# ret is the count

cv2.imshow('Closed image', imgbin) 
  
cv2.waitKey(0) 




