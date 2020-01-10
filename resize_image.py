import cv2

img = cv2.imread('miku_icon.png', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

dim = (40, 40)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imwrite('./miku_icon_resize.png', resized)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

