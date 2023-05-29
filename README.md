# PyImageProc Functions

This repository contains a collection of PyImageProc functions implemented in Python using the PIL (Python Imaging Library) package. These functions provide various operations such as resizing, rotation, grayscale conversion, thresholding, cropping, text application, and mosaic effect on images.

## Purpose

The purpose of the PyImageProc Functions package is to provide a simplified interface for performing basic image processing operations using the Pillow library in Python. This package aims to enhance the usability of Pillow by offering a set of functions that streamline common PyImageProcs.

The functions provided in this package allow you to easily resize images, rotate them at various angles, convert them to grayscale, apply thresholding to create binary images, crop specific regions of interest, add text overlays to images, and create mosaic effects.

By abstracting away the complexities of the Pillow library, this package aims to make PyImageProc tasks more accessible and user-friendly for developers who need to perform such operations on images.


## Buy Me A Coffee ☕️

<a href="https://www.buymeacoffee.com/altaysakarya" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


## Functions

- `resize_image(image_path, new_width, new_height, file_name="resized_image", save_path="")`: Resizes an image to the specified width and height.
- `rotate_image(image_path, angle, file_name="rotated_image", save_path="")`: Rotates an image by the specified angle.
- `apply_grayscale(image_path, file_name="grayscale_image", save_path="")`: Converts an image to grayscale.
- `apply_threshold(image_path, threshold, file_name="thresholded_image", save_path="")`: Applies a threshold to an image, converting it to a binary image based on the threshold value.
- `crop_image(image_path, x, y, width, height, file_name="cropped_image", save_path="")`: Crops an image to the specified region of interest.
- `apply_text(image_path, text, position, font_size, file_name="text_image", save_path="")`: Applies text to an image at the specified position.
- `apply_mosaic(image_path, block_size, file_name="mosaic_image", save_path="")`: Applies a mosaic effect to an image by reducing the resolution and then resizing back.

## Usage

1. Install the required dependencies by running the following command:

```
pip install Pillow
```


2. Import the necessary functions from the `pyimageproc` module:
```python
from pyimageproc import resize_image, rotate_image, apply_grayscale, apply_threshold, crop_image, apply_text, apply_mosaic
```

3. Use the functions to manipulate your images. Here's an example:

```python
resize_image("input_image.jpg", 800, 600, save_path="output/")
rotate_image("input_image.jpg", 45, save_path="output/")
apply_grayscale("input_image.jpg", save_path="output/")
apply_threshold("input_image.jpg", 128, save_path="output/")
crop_image("input_image.jpg", 100, 100, 400, 300, save_path="output/")
apply_text("input_image.jpg", "Hello, World!", (50, 50), 24, save_path="output/")
apply_mosaic("input_image.jpg", 10, save_path="output/")
```

4. Replace `"input_image.jpg"` with the path to your actual image file. Adjust the function arguments according to your requirements. The manipulated images will be saved in the specified save_path directory.

