import os, csv, shutil, sys
import urllib.request
from PIL import Image

def fetch_images(name_of_dataset, folder, max_images):
    failed = 0
    success = 0

    try:
        os.mkdir(folder)
    except OSError as error:
        print('Skipping folder creation... They already exist!')
    with open(os.getcwd() + '\\' + name_of_dataset, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) > 3 and row[3] != '':
                print('Found image named: ' + row[0] + ' and URL: ' + row[3])
                try:
                    urllib.request.urlretrieve(row[3], folder + '\\' + row[0] + '.jpg')
                    print('Successfully downloaded ' + row[0])
                    success = success + 1
                except (urllib.error.HTTPError, ValueError) as error:
                    print('Failed to download ' + row[0])
                    failed = failed + 1
                if max_images <= success: break
    print('\n===========================================================================')
    print(f'Finished {folder} with {success} images downloaded and {failed - 1} images skipped')
    print('===========================================================================\n')