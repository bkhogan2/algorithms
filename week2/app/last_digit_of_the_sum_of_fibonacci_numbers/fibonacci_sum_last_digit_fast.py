# Uses python3
import sys
sys.path.append('../')
from fibonacci_number.fibonacci_table import calc_fib

def fibonacci_sum_fast(n):
    fn_sum = calc_fib(n+2) - 1
    
    return  fn_sum % 10

n = int(input())

print(fibonacci_sum_fast(n))
