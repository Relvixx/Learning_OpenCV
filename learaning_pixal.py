import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Correct path to your image
img = Image.open("C:\Volume D\90 day,s robotics challenge\Learning_OpenCV\WhatsApp Image 2025-12-21 at 9.42.14 AM.jpeg")
"""img.sho"""
img_arr = np.array(img)
"""plt.imshow(img_arr)
plt.show()"""
img1 = img_arr.copy()
img2 = img_arr.copy()
img3 = img_arr.copy()

"""img1[:, : , 0] = 0
plt.imshow(img1)
plt.show()"""

"""img2[:, : , 1] = 0
plt.imshow(img2)
plt.show()"""

"""img3[:, : , 2] = 0
plt.imshow(img3)
plt.show()"""
