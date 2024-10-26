import os
import numpy as np
import cv2

# Define paths
DATA_DIR = "../data/food-101/images"
PROCESSED_DIR = "../data/processed_images"

# Create a directory for processed images
if not os.path.exists(PROCESSED_DIR):
    os.makedirs(PROCESSED_DIR)

def load_and_resize_image(image_path, size=(224, 224)):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Warning: Unable to load image at {image_path}.")
        return None
    img_resized = cv2.resize(img, size)
    return img_resized

def normalize_image(image):
    return image / 255.0

def preprocess_image(image_path):
    img = load_and_resize_image(image_path)
    if img is None:
        raise ValueError(f"Could not load image at path: {image_path}")
    image_normalized = normalize_image(img)
    return image_normalized


# Function to preprocess images
def preprocess_images(data_dir, processed_dir):
    for category in os.listdir(data_dir):
        category_path = os.path.join(data_dir, category)
        if os.path.isdir(category_path):  # Check if it's a directory
            print(f"Processing category: {category}")
            for img_file in os.listdir(category_path):
                img_path = os.path.join(category_path, img_file)
                print(f"Loading image: {img_path}")
                processed_image = preprocess_image(img_path)
                if processed_image is not None:
                    processed_img_path = os.path.join(processed_dir, category)
                    if not os.path.exists(processed_img_path):
                        os.makedirs(processed_img_path)
                    cv2.imwrite(os.path.join(processed_img_path, img_file), processed_image * 255)
                    print(f"Saved processed image to: {os.path.join(processed_img_path, img_file)}")
                else:
                    print(f"Skipping file {img_file} due to loading error.")
                    
if __name__ == "__main__":
    preprocess_images(DATA_DIR, PROCESSED_DIR)
    print("Image preprocessing complete!")