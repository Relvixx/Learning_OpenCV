import numpy as np
import matplotlib.pyplot as plt
import cv2


img1 = np.zeros(shape=(500, 500, 3) , dtype=np.int32)
print(img1.shape)

cv2.rectangle(img1, pt1=(300,300), pt2=(400,400), color=(135,130,180), thickness=5)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img1, text="RAHUL choudhary" ,org=(25,250), fontFace= font, fontScale=1, color=(80,140,240) , thickness=2)

img3 = np.zeros(shape=(500,500,3), dtype=np.int32)
vertice = np.array([[100,50],[300,250],[200,180],[400,50]], dtype=np.int32)
cv2.polylines(img3, [vertice] , isClosed=True, color=(180,45,60), thickness=2)

vertice2 = np.array([[(450, 250), (309, 439), (140, 404), (140, 96), (309, 61)]], dtype=np.int32)
cv2.polylines(img3, [vertice2] , isClosed=True, color=(60,45,100), thickness=2)


plt.imshow(img3)
plt.show()
