#!/bin/bash

RESIZE_CMD_PATH="~/Documents/code/my_py/resizeImg/resizeImg.py"
TO_WEBP_CMD_PATH="~/Documents/code/my_py/resizeImg/to_webp.py"
IMAGES_PATH="./"

python3 $RESIZE_CMD_PATH $IMAGES_PATH .25
python3 $TO_WEBP_CMD_PATH $IMAGES_PATH
rm $IMAGES_PATH*.jpg

for filename in $IMAGES_PATH*_resized.webp; do 
    [ -f "$filename" ] || continue
    mv "$filename" "${filename/_resized.webp/.webp}"

done
