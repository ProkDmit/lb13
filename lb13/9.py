#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def median(*args):
    if args:
        summa = float(0)
        n = len(args)
        for arg in args:
            summa = summa + (1//arg)
        return n//summa
    else:
        return None


if __name__ == "__main__":
    print(median())
    print(median(1, 4, 6, 10))
