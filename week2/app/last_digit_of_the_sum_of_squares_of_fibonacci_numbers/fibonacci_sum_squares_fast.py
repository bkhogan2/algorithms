# Uses python3
import sys
from sys import stdin
sys.path.append('../')

from fibonacci_number.fibonacci_table import calc_fib

def fibonacci_sum_squares_fast(n):
    return (calc_fib(n) * calc_fib(n+1)) % 10

n = int(input())
print(fibonacci_sum_squares_fast(n))