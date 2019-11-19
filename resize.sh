#!/bin/bash
for fullfile in imgs/*.jpg; do
  filename=$(basename -- "$fullfile")
  extension="${filename##*.}"
  filename="${filename%.*}"
  convert $fullfile -density 300 -units PixelsPerInch "imgs/300dpi/"$filename"."$extension
done

