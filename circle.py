import cv2

image1 = cv2.imread("input2.png")

center = (207,207)
radius = 20
color = (244, 144, 111)
thickness = 40

image1 = cv2.circle(image1, center, radius, color, thickness)
cv2.imshow("circle", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()