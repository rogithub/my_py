#!/bin/bash

RESIZE_CMD_PATH="./resizeImg.py"
TO_WEBP_CMD_PATH="./to_webp.py"
IMAGES_PATH="./"

procesar_imagenes () {
    # si param 1 no es directorio, salir
    if [ ! -d "$1" ]; then
	showHelp()
	exit 1
    fi

    # si param 2 no es numero salir
    if [![ "$2" =~ ^[0-9]+$ ]]; then
	showHelp()
	exit 1
    fi

    IMAGES_PATH=${$1/}

    python3 $RESIZE_CMD_PATH $IMAGES_PATH $2
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
  echo "Uso: ./resizeFiles.sh FOLDER REDUCCION" >&2
  echo "Ejemplo reducir a la mitad"
  echo ":$ ./resizeFiles.sh ~/imagenes .5" >&2
}


https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Parameter-Expansion
https://stackoverflow.com/questions/9018723/what-is-the-simplest-way-to-remove-a-trailing-slash-from-each-parameter
