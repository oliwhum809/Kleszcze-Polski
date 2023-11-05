import os
from PIL import Image
import glob

try:
    os.mkdir('manipulated_data_set')
    for genom in ['Ixodes', 'Dermacentor', 'Amblyomma']:
        os.mkdir('manipulated_data_set\\' + genom)
except OSError as error:
    print('Skipping folder creation... They already exist!')
for folder in glob.glob(os.getcwd() + '\\Mini_Bejbikowy_Zestawik_Kleszczy' + '\\*'):
    for image_path in  glob.glob(folder + '\\*'):
        image = Image.open(image_path)
        image = image.resize((320, 320))
        new_image_path = image_path.split('\\')
        new_image_path[-3] = 'manipulated_data_set'
        image.save('\\'.join(new_image_path))