# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
