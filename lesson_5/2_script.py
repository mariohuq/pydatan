#!/usr/bin/env python3
while True:
    try:
        s = input()
        print(s*2)
    except EOFError:
        break
