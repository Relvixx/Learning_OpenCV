import cv2

location = input("Enter your Image Location")

img = cv2.imread(f"{location}")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

prefrenace = input("What do you want Save or Show")

if(prefrenace=="save"):
    cv2.imwrite("gray.png",gray)
    print("your image has been save sucessfully")

elif(prefrenace == "show"):
    cv2.imshow("gray_scale", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




