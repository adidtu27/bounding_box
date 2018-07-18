import cv2
import numpy as np 
 
img = cv2.pyrDown(cv2.imread('EiffelTower.png',1))
 
# threshold image
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                25, 255, cv2.THRESH_BINARY)
# find contours and get the external one
image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,
                cv2.CHAIN_APPROX_SIMPLE)
 
# with each contour, draw boundingRect in green
# a minAreaRect in red and
# a minEnclosingCircle in blue
for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    # draw a green rectangle to visualize the bounding rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
    # get the min area rect
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    # convert all coordinates floating point values to int
    box = np.int0(box)
    # draw a red 'nghien' rectangle
    cv2.drawContours(img, [box], 0, (0, 0, 255))
 
 
print(len(contours))
cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
 
cv2.imshow("Contour", img)
 
ESC = 27
cv2.waitKey(0)
cv2.destroyAllWindows()