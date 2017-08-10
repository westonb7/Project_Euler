#!/bin/python
import sys

t = int(raw_input().strip())
def sum_factors_of_n_below_k(k, n):
    m = (k-1) // n
    return n * m * (m+1) // 2

def solution_01(m):
    return (sum_factors_of_n_below_k(m, 3) + 
            sum_factors_of_n_below_k(m, 5) - 
            sum_factors_of_n_below_k(m, 15))
for a0 in xrange(t):
    n = int(raw_input().strip())
    print solution_01(n)
