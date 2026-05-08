import cv2
import numpy as np

def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 1. Pixel ka BGR color nikalo (hint: row aur column ka order yaad rakhna)
        bgr_color = img[y,x]
        print(f"BGR: {bgr_color}")

        # 2. BGR ko HSV mein convert karo
        bgr_array = np.uint8([[bgr_color]])
        hsv_array = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2HSV)
        
        hsv_color = hsv_array[0][0]
        print(f"HSV: {hsv_color}")
        print("-" * 20)

# 3. 'image_58d9dd.png' ko load karo
img = cv2.imread(r"C:\\Volume D\\90 day,s robotics challenge\\Learning_OpenCV\\WhatsApp Image 2025-12-21 at 9.42.14 AM.jpeg")

# Image ko display karo
cv2.imshow('Color Picker', img)

# 4. Mouse callback function lagao (humare function ka naam yahan aayega)
cv2.setMouseCallback('Color Picker', get_color)

# 5. Window ko open rakho jab tak key press na ho
cv2.waitKey(0)