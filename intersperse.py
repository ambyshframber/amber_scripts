#!/usr/bin/env python3

from sys import stdin
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument("input", action="store", nargs="*", default="-")
p.add_argument("-c", action="store", default="👏")
a = p.parse_args()

if a.input == "-":
    input_list = stdin.read().split(" ")
else:
    if type(a.input) == type([]):
        input_list = a.input
    else:
        input_list: "list[str]" = a.input.split(" ")

print(a.c.join(input_list))
