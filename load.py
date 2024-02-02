import cv2
import matplotlib.pyplot as plt
#Load an image from file
image_path = r'/Users/mugishap/Documents/Precieux/Lessons/Y3/Embedded Systems/Term 2/projects/lena-opencv/lena.jpg'
image = cv2.imread(image_path)
#Display the image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()