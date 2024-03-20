import cv2

image1 = cv2.imread("input1.png")
startpoint = (0,0)
endpoint = (250,250)
color = (244, 144, 111)
thickness = 8

image1 = cv2.line(image1, startpoint, endpoint, color, thickness)
cv2.imshow("originalimage", image1)
cv2.imshow("newimage", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
