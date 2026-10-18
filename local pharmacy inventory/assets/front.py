
import cv2

img = input("Enter image name: ")
image = cv2.imread("/home/gangotri/Documents/project/gng/local pharmacy inventory/assets/"+img + ".png", cv2.IMREAD_UNCHANGED)

if image is None:
    print("Image not found!")
    exit()

# Invert RGB/BGR colors, preserve alpha transparency
if len(image.shape) == 3 and image.shape[2] == 4:
    negative_image = image.copy()
    negative_image[:, :, :3] = cv2.bitwise_not(image[:, :, :3])
else:
    negative_image = cv2.bitwise_not(image)

cv2.imwrite(img + "_dark.png", negative_image)

cv2.imshow("Original Image", image)
cv2.imshow("Negative Image", negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
