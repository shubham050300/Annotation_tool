import numpy as np
import cv2

from collections import Counter



# def imshow_components(labels):
#     # Map component labels to hue val
#     label_hue = np.uint8(179*labels/np.max(labels))
#     blank_ch = 255*np.ones_like(label_hue)
#     labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

#     # cvt to BGR for display
#     labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

#     # set bg label to black
#     labeled_img[label_hue==0] = 0

#     cv2.imshow('labeled.png', labeled_img)
#     cv2.waitKey()




imgor = cv2.imread("../../../Downloads/hole/canvas.png", 1);

img = imgor[:, :, 2]
# img[img==255] = 1


# img_erosion = cv2.erode(img, kernel=None, iterations=1) 

# img_dilation = cv2.dilate(img, kernel=None, iterations=1) 

imgclose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=None)
imgbin = cv2.threshold(imgclose, 200, 255, cv2.THRESH_BINARY)[1]

ret, labels = cv2.connectedComponents(imgbin)

for i in range(1, ret+1):
	xpoints = (labels==i).nonzero()[0]
	ypoints = (labels==i).nonzero()[1]

	if(xpoints.shape[0] < 10):
		print("here")
		for j in xrange(xpoints.shape[0]):
			imgbin[xpoints[j]][ypoints[j]] = 0




# imgbin is the final binary image ie 0 or 255


# Finding contours for the thresholded image
# im2, contours, hierarchy = cv2.findContours(imgbin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



# for i in range(1, ret+1):
# 	xpoints = (labels==i).nonzero()[0]
# 	ypoints = (labels==i).nonzero()[1]

# 	points = np.zeros((xpoints.shape[0] , 2))

# 	points[:, 0] = xpoints
# 	points[:, 1] = ypoints  



#     cv2.imshow('labeled.png', drawing)
#     cv2.waitKey()


# Counter(labels.flatten().tolist())


# imshow_components(labels)


# cv2.imshow('Closed image', imgclose) 
# # cv2.imshow('Input', img) 
# # cv2.imshow('Erosion', img_erosion) 
# # cv2.imshow('Dilation', img_dilation) 

cv2.imshow('Closed image', imgbin) 
  
cv2.waitKey(0) 




# for i in range(img[:, :, 0].shape[0]):
# 	for j in range(img[:, :, 0].shape[1]):
# 		# print(str(i) + " " + str(j))
# 		if not (img[i,j, 0] ==0 and img[i,j, 1] ==0 and img[i,j, 2] ==0):
# 			print(img[i][j])
