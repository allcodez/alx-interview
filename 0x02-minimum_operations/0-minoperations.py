#!/usr/bin/python3
""" Script computes a minimum operations
    needed in a CopyAll - Pastetask
"""

def minOperations(n):
    if n < 2:
        return 0
    list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                list.append(i)
    return sum(list)
