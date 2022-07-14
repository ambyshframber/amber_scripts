#!/usr/bin/env python3

from sys import stdin, argv
from hashlib import sha256
from math import sin, cos

if len(argv) == 1:
    input_str = stdin.read()
else:
    input_str = " ".join(argv[1:])

h = sha256()
h.update(bytearray(input_str, "utf-8"))

val = sin(cos(h.digest()[0] * 12965))
print(str(val > 0).lower())
