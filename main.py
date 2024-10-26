import cv2
import numpy as np
from matplotlib import pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

def load_and_resize_image(image_path, size=(224, 224)):
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, size)
    return img_resized

def normalize_image(image):
    return image / 255.0

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

def preprocess_image(image_path):
    img = load_and_resize_image(image_path)
    image_normalized = normalize_image(img)
    return image_normalized

if __name__ == "__main__":
    image_path = 'peanut.jpg'
    processed_image = preprocess_image(image_path)

    # Display the image
    plt.imshow(processed_image)
    plt.axis('off')  # Hide axes for better view
    plt.show()