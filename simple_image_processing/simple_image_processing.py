import numpy as np
from PIL import Image

def read_image(file_path):
    """Read an image file and return as numpy array."""
    return np.array(Image.open(file_path))

def save_image(image, file_path):
    """Save a numpy array as an image file."""
    Image.fromarray(image).save(file_path)

def grayscale(image):
    """Convert an image to grayscale."""
    return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

def invert(image):
    """Invert the colors of an image."""
    return 255 - image

def adjust_brightness(image, factor):
    """Adjust the brightness of an image."""
    return np.clip(image * factor, 0, 255).astype(np.uint8)