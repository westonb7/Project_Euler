#!/bin/python
import math
import sys

def primer(n):
    m = n
    x = 1
    if not m % 2:
        while not m % 2:
            m = m//2
            x *= 2
            if m == 1:
                return 2
    lm = int(math.ceil(math.sqrt(m)))
    while True:
        lm = int(math.ceil(math.sqrt(m)))
        j = 1
        for i in range (3, lm + 1, 2):
            if m%i == 0:
                m = m//i
                j = 0 
                x *= i
                break
            elif i == lm and m == n:
                return m
        if j == 1:
            return n//x
        j = 1

t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    print primer(n)
