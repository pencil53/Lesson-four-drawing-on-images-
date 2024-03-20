import cv2

image1 = cv2.imread("input2.png")
font = cv2.FONT_HERSHEY_SIMPLEX
origin = (100,100)
fontScale = 1
color = (244, 144, 111)
thickness = 5

image1 = cv2.putText(image1, "Hello!", origin, font, fontScale, color, thickness)
cv2.imshow("text",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()