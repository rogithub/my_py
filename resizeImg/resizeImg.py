#!/usr/bin/python
from PIL import Image
import os, sys

size = 1024, 1024

def resize(path):
    dirs = os.listdir( path )
    for item in dirs:
        if os.path.isfile(path+item):
            with Image.open(path+item) as im:                                
                imResize = im.thumbnail(size) 
                imResize.save(f + '_resized.jpg', 'JPEG')

if __name__ == "__main__":
    path = sys.argv[1];
    print('Resizing to 1024 x 1024 max path={}'.format(path))
    resize(path)
    print ('Done.')
