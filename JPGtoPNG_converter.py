from PIL import Image
import sys
import os

# Use "python converter.py ./originalFolder/ ./destinationFolder/" in command line
path1 = sys.argv[1]
path2 = sys.argv[2]

if not os.path.exists(path2):
    os.makedirs(path2)

for filename in os.listdir(path1):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path1}{filename}')
    img.save(f'{path2}{clean_name}.png', 'png')
    print('Images saved!')

