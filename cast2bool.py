#!/usr/bin/env python3

from sys import stdin
from hashlib import sha256
from argparse import ArgumentParser
from math import sin, cos

p = ArgumentParser()
p.add_argument("input", action="store", nargs="*", default="-")
a = p.parse_args()

if a.input == "-":
    input_str = stdin.read()
else:
    if type(a.input) == type([]):
        input_str = " ".join(a.input)
    else:
        input_str = a.input

h = sha256()
h.update(bytearray(input_str, "utf-8"))

val = sin(cos(h.digest()[0] * 12965))
print(str(val > 0).lower())
