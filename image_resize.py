import cv2

img= cv2.imread("99.jpg",cv2.IMREAD_UNCHANGED)
print("Original dimensions",img.shape)

scale_percent= 150
width= int(img.shape[1]*scale_percent/100)
height= int(img.shape[0]*scale_percent/100)
dim= (width, height)

resized= cv2.resize(img, dim, interpolation= cv2.INTER_NEAREST)
print("resized dimensions",resized.shape)
cv2.imshow("resized image", resized)
cv2.imshow("original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
