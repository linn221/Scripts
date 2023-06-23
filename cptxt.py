#! /usr/bin/env python3
import pyperclip, sys
file = sys.argv[1]
with open(file) as f:
    txt = f.read()
pyperclip.copy(txt)
