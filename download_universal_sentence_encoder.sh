#!/bin/bash

$DIR='models'
if [ "$(ls -A $DIR)" ]; then
    echo "models folder is not empty skipping download"
else
    echo "$DIR is Empty"
    wget https://tfhub.dev/google/universal-sentence-encoder/4?tf-hub-format=compressed
fi
