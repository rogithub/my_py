#!/bin/bash

for filename in *_resized.webp; do 
    [ -f "$filename" ] || continue
    mv "$filename" "${filename/_resized.webp/.webp}"

done
