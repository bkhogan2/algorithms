# Uses python3
import sys
from gcd_euclid import gcd_euclid

def lcm_euclid(a, b):
    return (a*b) / gcd_euclid(a,b)

a = int(input())
b = int(input())

print(lcm_euclid(a,b))
