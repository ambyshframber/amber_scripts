#!/usr/bin/env python3

from sys import stdin
import random

input_str = stdin.read().split("\n")
print(random.choice(input_str))
