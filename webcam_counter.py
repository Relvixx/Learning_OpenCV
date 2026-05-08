import cv2

# 1. Image load karna (apni photo ka naam yahan likho)
cap =  cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 2. Grayscale mein convert karna
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 3. Gaussian Blur apply karna (noise hatane ke liye)
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)


    # 4. Canny Edge Detection (kinare nikalna)
    edges = cv2.Canny(blurred_frame, 15, 100)
    # 5. Contours find karna
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6. Original image par green color se contours draw karna
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # 7. Total count terminal/console mein print karna
    print(f"Total Coins: {len(contours)}")

    # 8. Results screen par display karna
    # Hum original (contours ke sath) aur edges dono ki windows open kar rahe hain
    cv2.imshow("Detected Coins", frame)
    cv2.imshow("Canny Edges (Computer Vision)", edges)

   # 8. 'q' dabane par loop break karna
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()