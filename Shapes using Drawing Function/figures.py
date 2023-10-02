import cv2
import numpy as np
img = np.zeros((400, 400, 3), dtype=np.uint8)

#Line
cv2.line(img, (50, 50), (350, 350), (0, 0, 255), 2)

#Rectangle
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 2)

#Ellipse
cv2.ellipse(img, (200, 200), (100, 50), 0, 0, 360, (255, 0, 0), 2)

#Circle
cv2.circle(img, (200, 200), 50, (0, 255, 255), 2)

#Displaying image
cv2.imshow("Geometric Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
