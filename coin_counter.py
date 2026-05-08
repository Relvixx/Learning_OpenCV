import cv2

# 1. Image load karna (apni photo ka naam yahan likho)
img = cv2.imread(r"C:\\Volume D\\90 day,s robotics challenge\\Learning_OpenCV\\room.jpg.jpeg")

#RESIZE
img = cv2.resize(img, (800, 600))

# 2. Grayscale mein convert karna
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Gaussian Blur apply karna (noise hatane ke liye)
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)


# 4. Canny Edge Detection (kinare nikalna)
edges = cv2.Canny(blurred_img, 15, 100)
# 5. Contours find karna
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 6. Original image par green color se contours draw karna
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# 7. Total count terminal/console mein print karna
print(f"Total Coins: {len(contours)}")

# 8. Results screen par display karna
# Hum original (contours ke sath) aur edges dono ki windows open kar rahe hain
cv2.imshow("Detected Coins", img)
cv2.imshow("Canny Edges (Computer Vision)", edges)

# Kisi bhi key ke press hone ka wait karna aur phir windows close karna
cv2.waitKey(0)
cv2.destroyAllWindows()