#!/bin/bash

RESIZE_CMD_PATH="./resizeImg.py"
TO_WEBP_CMD_PATH="./to_webp.py"
IMAGES_PATH="./"

procesar_imagenes () {
    # si param 1 no es directorio, salir
    if [ ! -d "$1" ]; then	
	echo 'Folder not found:' $1 >&2
	exit 1
    fi

    IMAGES_PATH=$(dirname "$1")"/"$(basename "$1")

    # rename *.jpeg to .jpg
    for filename in $IMAGES_PATH/*.jpeg; do 
        [ -f "$filename" ] || continue
        mv "$filename" "${filename/.jpeg/.jpg}"
    done

    python3 $RESIZE_CMD_PATH $IMAGES_PATH
    python3 $TO_WEBP_CMD_PATH $IMAGES_PATH
    rm $IMAGES_PATH/*.jpg

    for filename in $IMAGES_PATH/*_resized.webp; do 
	[ -f "$filename" ] || continue
	mv "$filename" "${filename/_resized.webp/.webp}"
    done
}

showHelp()
{
  echo "Cambia el tamaño de jpg y los convierte a .webp" >&2
  echo "Uso: ./convert_resize_jpg_to_webp.sh [Dir-Path]" >&2
  echo ""
  echo "Ejemplo"
  echo "$ ./convert_resize_jpg_to_webp.sh ~/imagenes" >&2
}

if [ $# -ne 1 ] ; then
  showHelp
  exit 1
fi

procesar_imagenes $1
