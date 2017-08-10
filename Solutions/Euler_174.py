#!/bin/python
import math
j=0

n = int(raw_input())
ar = [0]*n
for i in range(1, n+1):
    ar[i-1] = int(raw_input())
k=max(ar)

types =[0]*(k+100)
for i in range (2,int(math.sqrt(k)), 2):
    b=2
    while True:
        product = i * (i + b)
        if product > k:
            break
        types[product] += 1
        b += 2      
    
result=[0]*(k+100)
for i in range(0, k+2):
    if types[i] >= 1 and types[i] <= 10:
        result[i] = result[i-1] + 1
    else:
        result[i] = result[i-1]

for i in range(1, n+1):
    print(result[ar[i-1]])
