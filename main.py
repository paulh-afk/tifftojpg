import os
from PIL import Image

path = os.getcwd()

for file in os.listdir(path + '/src-img'):
    file_split = file.split('.')

    file_name = ''.join([file_split[i] for i in range(len(file_split) - 1)])
    format = file_split[-1].lower()
    if format != 'tiff' and format != 'tif':
        continue

    already_exists = os.path.exists(
        '{path}/dest-img/{file}.jpg'
        .format(path=path,
                file=file_name))
    if already_exists:
        continue

    file_path = '{path}/{dir}/{file}'.format(path=path,
                                             dir='/src-img',
                                             file=file)
    img = Image.open(file_path)
    img.save("dest-img/" + file_name + ".jpg")
