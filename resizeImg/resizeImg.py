#!/usr/bin/python
from PIL import Image
import os, sys

def get_ratio(size, ratio):
    new_size = (
        int(size[0] / (1/ratio)),
        int(size[1] / (1/ratio))
    )
    return new_size

def resize(path, ratio):
    dirs = os.listdir( path )
    for item in dirs:
        if os.path.isfile(path+item):
            with Image.open(path+item) as im:
                size = get_ratio(im.size, ratio)
                f, e = os.path.splitext(path+item)
                imResize = im.resize(size, Image.ANTIALIAS)
                imResize.save(f + '_resized.jpg', 'JPEG', quality=90)

if __name__ == "__main__":
    path = sys.argv[1];
    ratio = float(sys.argv[2]);    
    print('Resizing path={} ratio={}'.format(path, ratio))
    print('ratio = 0.5  # where 0.5 is half size, 2 is double size')
    resize(path, ratio)
    print ('Done.')
