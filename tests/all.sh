#!/bin/bash

for filename in "examples"/*; do
    echo "Testing '$filename'"
    name=$(basename -- "$filename")
    pyccb $filename -o build/"${name%.*}.sh"
    if [ $? != "0" ]; then
        echo "${name} failed!"
    fi
    echo -e "\n"
done
