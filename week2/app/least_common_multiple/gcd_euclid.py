# Uses python3
import sys

def gcd_euclid(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a % b)
    
    return -1

a = int(input())
b = int(input())

print(gcd_euclid(a,b))