#!/bin/python
import sys

def fibbo(n):
    jk = 1
    fn = 1
    lv = 0
    ev = 0
    while fn < n:
        lv = fn
        fn += jk
        jk = lv
        if not fn % 2 and fn < n:
            ev += fn
    return ev
                
t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    print fibbo(n)
