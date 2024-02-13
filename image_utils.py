from PIL import Image, ImageDraw, ImageFont


def resize_image(image_path, new_width, new_height, file_name=None, save_path=None):
    """
    Resizes an image to the specified width and height.

    Args:
        image_path (str): The path to the image file.
        new_width (int): The desired width of the resized image.
        new_height (int): The desired height of the resized image.
        file_name (str, optional): The name of the output file. Defaults to "resized_image".
        save_path (str, optional): The path to save the resized image. Defaults to the current directory.
    """
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height))
    if file_name is not None and save_path is not None:
        ext = image_path.split(".")[-1]
        resized_image.save(save_path + f"{file_name}.{ext}")
    else:
        return resized_image


def rotate_image(image_path, angle, file_name=None, save_path=None):
    """
    Rotates an image by the specified angle.

    Args:
        image_path (str): The path to the image file.
        angle (float): The angle of rotation in degrees.
        file_name (str, optional): The name of the output file. Defaults to "rotated_image".
        save_path (str, optional): The path to save the rotated image. Defaults to the current directory.
    """
    image = Image.open(image_path)
    rotated_image = image.rotate(angle)
    if file_name is not None and save_path is not None:
        ext = image_path.split(".")[-1]
        rotated_image.save(save_path + f"{file_name}.{ext}")
    else:
        return rotated_image


def apply_grayscale(image_path, file_name="grayscale_image", save_path=""):
    """
    Converts an image to grayscale.

    Args:
        image_path (str): The path to the image file.
        file_name (str, optional): The name of the output file. Defaults to "grayscale_image".
        save_path (str, optional): The path to save the grayscale image. Defaults to the current directory.
    """
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    ext = image_path.split(".")[-1]
    grayscale_image.save(save_path + f"{file_name}.{ext}")


def apply_threshold(image_path, threshold, file_name="thresholded_image", save_path=""):
    """
    Applies a threshold to an image, converting it to a binary image based on the threshold value.

    Args:
        image_path (str): The path to the image file.
        threshold (int): The threshold value for binarization.
        file_name (str, optional): The name of the output file. Defaults to "thresholded_image".
        save_path (str, optional): The path to save the thresholded image. Defaults to the current directory.
    """
    image = Image.open(image_path).convert("L")
    thresholded_image = image.point(lambda p: p > threshold and 255)
    ext = image_path.split(".")[-1]
    thresholded_image.save(save_path + f"{file_name}.{ext}")


def crop_image(image_path, x, y, width, height, file_name="cropped_image", save_path=""):
    """
    Crops an image to the specified region of interest.

    Args:
        image_path (str): The path to the image file.
        x (int): The x-coordinate of the top-left corner of the ROI.
        y (int): The y-coordinate of the top-left corner of the ROI.
        width (int): The width of the ROI.
        height (int): The height of the ROI.
        file_name (str, optional): The name of the output file. Defaults to "cropped_image".
        save_path (str, optional): The path to save the cropped image. Defaults to the current directory.
    """
    image = Image.open(image_path)
    cropped_image = image.crop((x, y, x + width, y + height))
    ext = image_path.split(".")[-1]
    cropped_image.save(save_path + f"{file_name}.{ext}")


def apply_text(image_path, text, position, font_size, file_name="text_image", save_path=""):
    """
    Applies text to an image at the specified position.

    Args:
        image_path (str): The path to the image file.
        text (str): The text to be applied to the image.
        position (tuple): The position (x, y) where the text will be drawn.
        font_size (int): The font size of the text.
        file_name (str, optional): The name of the output file. Defaults to "text_image".
        save_path (str, optional): The path to save the text image. Defaults to the current directory.
    """
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw.text(position, text, fill=(0, 0, 0), font=font)
    ext = image_path.split(".")[-1]
    image.save(save_path + f"{file_name}.{ext}")


def apply_mosaic(image_path, block_size, file_name="mosaic_image", save_path=""):
    """
    Applies a mosaic effect to an image by reducing the resolution and then resizing back.

    Args:
        image_path (str): The path to the image file.
        block_size (int): The size of the mosaic blocks.
        file_name (str, optional): The name of the output file. Defaults to "mosaic_image".
        save_path (str, optional): The path to save the mosaic image. Defaults to the current directory.
    """
    image = Image.open(image_path)
    width, height = image.size
    mosaic_image = image.resize((width // block_size, height // block_size))
    mosaic_image = mosaic_image.resize((width, height), Image.NEAREST)
    ext = image_path.split(".")[-1]
    mosaic_image.save(save_path + f"{file_name}.{ext}")
