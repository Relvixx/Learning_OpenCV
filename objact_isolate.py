import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # 1. BGR ko HSV mein convert karna
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 2. Green color ki limits define karna
    # Hue ko 35-85 kiya, aur Saturation/Value ko 30 tak kam kiya taaki thode dark greens/shadows bhi pakde jayein
    lower_green = np.array([35, 30, 30])
    upper_green = np.array([85, 255, 255])
    
    # 3. Mask banana (Green pixels white ho jayenge, baaki black)
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Mask mein contours (shapes) dhundhna
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Har contour (green object) ke liye
    for c in contours:
        # Chhote-mote green dhabbon (noise) ko ignore karne ke liye condition
        # Agar object ka area 500 pixels se bada hai, tabhi box banao
        if cv2.contourArea(c) > 500:
            # Contour ka ek bounding box (x, y, w, h) nikalna
            x, y, w, h = cv2.boundingRect(c)
            
            # Original frame par Green Box banana aur Text likhna
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Soda-G Target", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # 4. Mask ko original frame par apply karna
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Teeno windows ek sath dikhana taaki difference samajh aaye
    cv2.imshow("1. Original Frame", frame)
    cv2.imshow("2. Mask (Black & White)", mask)
    cv2.imshow("3. Only Green Objects", result)
    
    # 'q' dabane par exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()