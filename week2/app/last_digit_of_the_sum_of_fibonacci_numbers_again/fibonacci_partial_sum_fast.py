# Uses python3
import sys
sys.path.append('../')

from fibonacci_number.fibonacci_table import calc_fib

def fibonacci_partial_sum_fast(from_, to):
    return (calc_fib(to + 2) - calc_fib(from_+ 1)) % 10


n = int(input())
m = int(input())

print(fibonacci_partial_sum_fast(m,n))