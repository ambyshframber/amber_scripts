# amber scripts

this is a collection of small utility scripts i use to make common tasks easier. current prereqs are python3 and bash.

make some symlinks from here into your ~/.local/bin folder or wherever else you have PATH pointed and you'll be able to run these from anywhere (i'll set up a makefile at some point i promise). you might also have to chmod +x them

## contents

### 8.sh

magic 8 ball. requires mpv for full functionality

### bitrot.py

simulated bitrot script. flips random bits in the input text to simulate what it would look like if your HDD was really dodgy

### cast2bool.py

deterministic pseudorandom ouija board

### intersperse.py

very 👏 useful 👏 python 👏 script  
`-c DELIM` changes the added character  
`-s` adds spaces between the words and the added character  
`-n` removes the newline from the end

### pig.lua

dice rolling game of some description

### scrabble.py

calculate the scrabble score of a given input. `-n` divides the score by the length, and `-s` does not add zero-score characters (whitespace, extended unicode etc) to the length

### scrablist.py

scrabble a list of inputs

### seive.py

seive of eratosthenes, for a laugh
