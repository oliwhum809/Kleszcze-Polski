import os
from PIL import Image
import glob

try:
    os.mkdir('manipulated_data_set')
    for lession in ['AK', 'BCC', 'BKL', 'DF', 'MEL', 'NV', 'SCC', 'VASC']:
        os.mkdir('manipulated_data_set\\' + lession)
except OSError as error:
    print('Skipping folder creation... They already exist!')
for folder in glob.glob(os.getcwd() + '\\combined_data_set' + '\\*'):
    for image_path in  glob.glob(folder + '\\*'):
        image = Image.open(image_path)
        image = image.resize((320, 320))
        new_image_path = image_path.split('\\')
        new_image_path[-3] = 'manipulated_data_set'
        image.save('\\'.join(new_image_path))