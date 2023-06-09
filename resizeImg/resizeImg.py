#!/usr/bin/python
from PIL import Image
import os, sys

size = 1040, 780

def resize(path):
    dirs = os.listdir( path )
    for item in dirs:
        if os.path.isfile(path+item):
            with Image.open(path+item) as im:                                
                imResize = im.thumbnail(size, PIL.Image.ANTIALIAS) 
                imResize.save(f + '_resized.jpg', 'JPEG')

if __name__ == "__main__":
    path = sys.argv[1];
    print('Resizing to 1040 x 780 max path={}'.format(path))
    resize(path)
    print ('Done.')
