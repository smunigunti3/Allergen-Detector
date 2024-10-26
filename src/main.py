import cv2
import numpy as np
from matplotlib import pyplot as plt
from data_preprocessing import preprocess_image

def main():
    image_path = 'peanut.jpg'
    preprocessed_image = preprocess_image(image_path)
    plt.imshow(preprocessed_image)
    plt.axis('off')  # Hide axes for better view
    plt.show()


if __name__ == "__main__":
    main()
    