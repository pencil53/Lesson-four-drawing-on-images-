import cv2

image1 = cv2.imread("input2.png")
startpoint = (0,0)
endpoint = (415,415)
color = (244, 144, 111)
thickness = 20

image1 = cv2.rectangle(image1, startpoint, endpoint, color, thickness)
cv2.imshow("rectangleimage", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()