# package_name

Description. 

The package Simple Image Processing is used to:
	- A basic image processing package with simple operations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install simple_image_processing

```bash
pip install simple_image_processing
```

## Usage

```python
from simple_image_processing import read_image, grayscale, save_image

# Read an image
img = read_image('path/to/image.jpg')

# Convert to grayscale
gray_img = grayscale(img)

# Save the result
save_image(gray_img, 'path/to/grayscale_image.jpg')
```
## Available Functions

- `read_image(file_path)`: Read an image file
- `save_image(image, file_path)`: Save an image file
- `grayscale(image)`: Convert image to grayscale
- `invert(image)`: Invert image colors
- `adjust_brightness(image, factor)`: Adjust image brightness

## Author
Lucas Ponte

## License
[MIT](https://choosealicense.com/licenses/mit/)