#!/usr/bin/env python3

from sys import stdin
from argparse import ArgumentParser

SCORES = ["", "aeilnorstu", "dg", "bcmp", "fhvwy", "k", "", "", "jx", "", "qz"]

p = ArgumentParser()
p.add_argument("input", action="store", nargs="*", default="-")
p.add_argument("-n", action="store_true", default=False)
a = p.parse_args()

if a.input == "-":
    input_str = stdin.read()
else:
    if type(a.input) == type([]):
        input_str = " ".join(a.input)
    else:
        input_str = a.input

def scrabble(s: str, normalise):
    s_lower = s.lower()
    total = 0
    length = 0
    for c in s_lower:
        total += scrabble_char(c)
        if not c.isspace():
            length += 1
    
    if normalise:
        total /= length
    
    return total

def scrabble_char(c):
    for i in range(len(SCORES)):
        if c in SCORES[i]:
            return i
    
    return 0

print(scrabble(input_str, a.n))