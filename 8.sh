#!/bin/sh

cd $(dirname $(realpath $0))

shuf -n1 8_responses.txt
mpv --no-terminal eight.wav &
