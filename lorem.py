#! /usr/bin/env python3
import sys, pyperclip

if len(sys.argv) == 1:
    num = 50
else:
    num = int(sys.argv[1])
t = ''
for _ in range(num):
    t += 'art '
pyperclip.copy(t)
