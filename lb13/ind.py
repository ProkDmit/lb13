#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def posle_sum(*args):
    if args:
        i = 0
        sum = 0
        k = n.count(0)
        for arg in args:
            if arg == 0:
                i += 1
            if i == k:
                sum += arg
        return sum
    else:
        return None


if __name__ == "__main__":
    n = [int(i) for i in input("Enter the n: ").split()]
    print("The sum of the arguments placed after the last argument equal to zero: "
          f"{posle_sum(*n)}"
          )
