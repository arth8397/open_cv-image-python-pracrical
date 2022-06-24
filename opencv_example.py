import cv2 
import os
image_path = r"C:\\Users\Lenovo\\Desktop\\Practicals\\opencv_install\\Master.jpg"
directory = r"C:\Users\Lenovo\Desktop\Practicals\opencv_install"

#reading image
img = cv2.imread(image_path, 1)
cv2.imshow("IMAGE", img)

#writing image
os.chdir(directory)
print("Before saving image:")
print(os.listdir(directory))
filename = 'NewImage.png'
cv2.imwrite(filename, img)
print("After saving image:")
print(os.listdir(directory))
print('Successfully Saved')

#conversing image
img = cv2.imread(image_path)
(row, col) = img.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) * 0.2
cv2.imshow('Grayscale Image', img)

#complementing image
imgcom = cv2.imread(image_path)
imgcom = cv2.bitwise_not(imgcom)
cv2.imshow("complement image", imgcom)

cv2.waitKey(0)
cv2.destroyAllWindows()