#!/bin/bash
#echo "$1

filename=$(echo $1)
fname="${filename%.*}"
out_fname="${fname}.txt"
edl_fname="${fname}.edl"

echo "converting to ${out_fname}"

ffmpeg -y -i "${filename}" -f ffmetadata "${out_fname}"

cat "${out_fname}" | python3 ~/convert.py > "${edl_fname}"

rm "${out_fname}"
