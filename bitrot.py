#!/usr/bin/env python3

import random
import sys

def bitrot(b):
    byte = ord(b)
    while random.random() > 0.9:
        byte ^= 1 << random.randrange(0,7)
    byte &= 0b0111_1111
    if byte < 0x20 or byte == 0x7f:
        if byte != 0xa and byte != 0xd:
            byte = 0x20
    return chr(byte)

inp_str = sys.stdin.read()

out_str = "".join([bitrot(c) for c in inp_str])
print(out_str)
