from fetch_images import fetch_images
import glob, os, sys

try:
    max_images = int(sys.argv[1])
    for image_base_file_path in glob.glob(os.getcwd() + '\\*.txt'):
        image_base_file_name = image_base_file_path.split('\\')[-1]
        fetch_images(image_base_file_name, image_base_file_name.split('.')[0], max_images)
except IndexError as error:
    print('Usage: script_name <max_images>')