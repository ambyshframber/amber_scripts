#!/usr/bin/env python3

from sys import stdin
from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument("input", action="store", nargs="*", default="-")
p.add_argument("-c", action="store", default="👏")
p.add_argument("-s", action="store_true", default=False)
p.add_argument("-n", action="store_true", default=False)
p.add_argument("-r", action="store_true", default=False)
a = p.parse_args()

if a.input == "-":
    input_list = stdin.read().split(" ")
else:
    input_list = []
    for i in a.input:
        input_list.extend(i.split(" "))

sep = a.c
if a.r:
    sep = "🚀"
if a.s:
    sep = f" {sep} "

msg = sep.join(input_list)

print(msg, end="")
if not a.n:
    print("")
