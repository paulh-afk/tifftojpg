import os
from PIL import Image

# Windows PATH
path = os.getcwd() + "\\src-img"

for file in os.listdir(path):
    format = file.split('.')[-1].lower()
    if format != 'tiff' and format != 'tif':
        continue
