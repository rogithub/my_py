#!/usr/bin/python
from PIL import Image
import os, sys

def get_size(im):    
    return 780, 1040 if img.size[0] > img.size[1] else 1040, 780

def resize(path):
    dirs = os.listdir( path )
    for item in dirs:
        if os.path.isfile(path+item):
            with Image.open(path+item) as im:
                print('Resizing initial {} x {}'.format(img.size[0], img.size[1]))
                size = get_size(im)
                print('Resizing to {} x {}'.format(size[0], size[1]))
                imResize = im.thumbnail(size, PIL.Image.Resampling.LANCZOS) 
                imResize.save(f + '_resized.jpg', 'JPEG')

if __name__ == "__main__":
    path = sys.argv[1];
    print('Resizing to 1040 x 780 max path={}'.format(path))
    resize(path)
    print ('Done.')
