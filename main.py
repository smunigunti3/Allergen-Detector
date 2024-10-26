import cv2
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('peanut.jpg')  # Make sure this image is in your project folder

# Convert from BGR (OpenCV default) to RGB for displaying with matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(img_rgb)
plt.axis('off')  # Hide axes for better view
plt.show()