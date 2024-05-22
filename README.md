# About Image-Shrinker
This Python script will automatically resize images and maintain their aspect ratio. It's useful for preparing image files to fine-tune or train image generation models.

## Notes and documentation

### Install the Pillow library
Install Pillow (PIL) if you haven't already:

`python -m pip install --upgrade pip`

### Functions and what they do 

**Function: resize_image(input_path, output_path):**

This function takes two parameters: input_path (the path to the original image) and output_path (the path where the resized image will be saved). It opens the image from input_path and calculates a scaling factor to adjust the image’s size while maintaining its aspect ratio.

If the image's longest side is greater than 1024 pixels, it resizes the image using the Lanczos filter, a high-quality downsampling filter. The resized image is then saved to output_path. If the image is already smaller than 1024 pixels,or whichever measure you choose, it saves the original image without resizing.

**Function: process_images(source_folder, target_folder='1024Images'):**

This function processes all images in a specified source_folder. It checks if a target folder exists for the resized images; if not, it creates one.

The function iterates over all files in the source_folder. If a file has an image extension (.png, .jpg, .jpeg), it constructs full paths for the source and target, and then calls resize_image to process each image.

### Summary
This script is useful for users needing to batch resize images for social media or applications like web optimization or machine learning, where uniform image dimensions may be required. It automates the tedious task of manually resizing images and ensures all processed images adhere to the specified size constraints while maintaining their original aspect ratios.
