import cv2
import matplotlib.pyplot as plt
#Load an image from file
image_path = '/Users/mugishap/Documents/Precieux/Lessons/Y3/Embedded Systems/Term 2/projects/lena-opencv/lena.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Apply Canny edge detection
edges = cv2.Canny(gray_image, 50, 150)
 #Display the edges
plt.imshow(edges, cmap='gray') 
plt.title('Edge Detection') 
plt.show()