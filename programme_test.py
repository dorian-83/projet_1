#!/bin/env python3

import re

if __name__=="__main__":
    # programme principal
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))


