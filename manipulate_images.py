import os, sys
from PIL import Image
import glob

args = sys.argv[1:]
data_set_name = args[0]

classes = [folder_path.split('/')[-1] for folder_path in glob.glob(os.getcwd() + '/' + data_set_name + '/*')]
manipulated_data_set_name = 'manipulated_' + data_set_name

try:
    os.mkdir(manipulated_data_set_name)
    for class_name in classes:
        os.mkdir(manipulated_data_set_name + '/' + class_name)
except OSError as error:
    print('Skipping folder creation... They already exist!')
for folder in glob.glob(os.getcwd() + '/' + data_set_name + '/*'):
    for image_path in  glob.glob(folder + '/*'):
        image = Image.open(image_path)
        image = image.resize((320, 320))
        new_image_path = image_path.split('/')
        new_image_path[-3] = manipulated_data_set_name
        image.save('/'.join(new_image_path))