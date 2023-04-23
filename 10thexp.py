import cv2
import numpy as np
from google.colab.patches import cv2_imshow
img = cv2.imread('apple.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)
kernel = np.ones((5,5),np.uint8)
dilated = cv2.dilate(edges, kernel, iterations = 1)
cv2_imshow(img)
cv2_imshow(gray)
cv2_imshow(blur)
cv2_imshow(edges)
cv2_imshow(dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()