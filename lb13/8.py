#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def median(*args):
    if args:
        summa = 0
        n = len(args)
        for arg in args:
            summa = summa + arg
        return summa // n
    else:
        return None


if __name__ == "__main__":
    print(median())
    print(median(1, 3, 9, 27, 81))
