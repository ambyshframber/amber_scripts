#!/bin/bash

stdin=$(cat)

for item in $stdin; do
    echo $item $(scrabble -ns $item)
done
