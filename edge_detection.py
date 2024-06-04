
import cv2
import matplotlib.pyplot as plt
image = cv2.imread(r"D:\Python Projects\Body Align\WIN_20240508_15_47_42_Pro.jpg", cv2.IMREAD_COLOR)
image = cv2.GaussianBlur(image, (3, 3), 0)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filtered_image = cv2.Laplacian(image_gray, cv2.CV_16S, ksize=3)

# Plot the original and filtered images
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(122)
plt.imshow(filtered_image, cmap='gray')
plt.title('LoG Filtered Image')

#save fig
plt.savefig(r"D:\Python Projects\Body Align\edge_detection.png")

plt.show()