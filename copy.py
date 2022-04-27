#!/usr/bin/env python3

import pyperclip
import sys

s = sys.stdin.read()
pyperclip.copy(s)
