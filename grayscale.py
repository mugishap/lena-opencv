import cv2
import matplotlib.pyplot as plt
#Load an image from file
image_path = '/Users/mugishap/Documents/Precieux/Lessons/Y3/Embedded Systems/Term 2/projects/lena-opencv/lena.jpg'
image = cv2.imread(image_path)
 #Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 #Display the grayscale image
plt.imshow(gray_image, cmap='gray') 
plt.title('Grayscale Image') 
plt.show()