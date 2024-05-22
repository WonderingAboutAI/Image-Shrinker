import os
from PIL import Image

def resize_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Calculate the scaling factor, keeping the aspect ratio
            scaling_factor = 1024 / max(img.size)
            if scaling_factor < 1:  # Only resize if the image is larger than 1024 on its longest side
                new_size = tuple(int(scaling_factor * dim) for dim in img.size)
                # Resize image using high-quality downsampling
                resized_img = img.resize(new_size, Image.LANCZOS)  # Use Image.LANCZOS
                resized_img.save(output_path)
                print(f"Resized and saved image to {output_path}")
            else:
                img.save(output_path)
                print(f"Image is smaller than 1024 pixels on the longest side, saved original to {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def process_images(source_folder, target_folder='1024Images'):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"Created directory {target_folder}")
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename)
            print(f"Processing {source_path}")
            resize_image(source_path, target_path)

# Example usage: specify the path to your images directory
source_directory = 'Your path here'
process_images(source_directory)
