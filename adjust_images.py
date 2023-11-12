import sys, os, glob, random
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import img_to_array, load_img

###################################################################################################################
###################################################################################################################

def generate_to_folder(number_of_images, generate_from, generate_to):
    counter = 0
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
    while(counter < number_of_images):
        for image_path in glob.glob(generate_from + '/*'):
            img = load_img(image_path)
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)
            datagen.flow(x, 
                         batch_size=1,
                         save_to_dir = generate_to,
                         save_prefix = image_path.split('/')[-1].split('.')[-2] + '_augmented',
                         save_format = image_path.split('/')[-1].split('.')[-1]).next()
            counter = counter + 1
            if counter >= number_of_images: break

def move_to_folder(number_of_images, move_from, move_to):
    counter = 0
    while(counter < number_of_images):
        images_paths = glob.glob(move_from + '/*')   
        random.shuffle(images_paths)    
        image_path = images_paths[0]
        image_name = image_path.split('/')[-1]
        new_image_path = move_to + '/' + image_name
        os.rename(image_path, new_image_path)
        counter = counter + 1

###################################################################################################################
###################################################################################################################

args = sys.argv[1:]
data_set_name = args[0]
train_number = int(args[1])
validation_number = int(args[2])

classes = [folder_path.split('/')[-1] for folder_path in glob.glob(os.getcwd() + '/' + data_set_name + '/*')]
adjusted_data_set_name = 'adjusted_' + data_set_name

try:
    os.mkdir(adjusted_data_set_name)
    for type in ['train', 'validate']:
        os.mkdir(adjusted_data_set_name + '/' + type)
        for class_name in classes:
            os.mkdir(adjusted_data_set_name + '/' + type + '/' + class_name)
except OSError as error:
    print('Skipping folder creation... They already exist!')
for folder in glob.glob(os.getcwd() + '/' + data_set_name + '/*'):
    train_folder = folder.split('/')
    train_folder[-2] = adjusted_data_set_name + '/train'
    train_folder = '/'.join(train_folder)
    validation_folder = folder.split('/')
    validation_folder[-2] = adjusted_data_set_name + '/validate'
    validation_folder = '/'.join(validation_folder)
    images_paths = glob.glob(folder + '/*')
    if (len(images_paths) > validation_number and len(images_paths) >= validation_number + train_number):
        move_to_folder(validation_number, folder, validation_folder)
        move_to_folder(train_number, folder, train_folder)
    elif (len(images_paths) > validation_number and len(images_paths) < validation_number + train_number):
        generate_to_folder(validation_number + train_number - len(images_paths), folder, train_folder)
        move_to_folder(validation_number, folder, validation_folder)
        move_to_folder(len(images_paths) - validation_number, folder, train_folder)
    else:
        generate_to_folder(validation_number - len(images_paths), folder, validation_folder) 
        generate_to_folder(train_number, folder, train_folder)
        move_to_folder(len(images_paths), folder, validation_folder)