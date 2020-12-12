#!/bin/bash
#echo "$1

filename=$(echo $1)
fname="${filename%.*}"
temp_fname="${fname}.txt"
edl_fname="${fname}.edl"


if [ -f "$edl_fname" ]; then
    echo "$edl_fname already exists."
else
    echo "$edl_fname does not exist. Converting."
    ffmpeg -y -i "${filename}" -f ffmetadata "${temp_fname}"
    cat "${temp_fname}" | python3 ~/convert.py > "${edl_fname}"
    rm "${temp_fname}"
fi
