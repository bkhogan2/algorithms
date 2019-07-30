# Uses python3
import sys
sys.path.append('/Users/brianhogan/Developer/algorithms/week2/app')

from fibonacci_number.fibonacci_table import calc_fib
# from .last_digit_of_fibonacci_number.fibonacci_last_digit_table import get_fibonacci_last_digit_table
n = int(input())

# for N in get_fibonacci_last_digit_table(n):
#     print(N, end=" ")

for N in range(n):
    print(calc_fib(N), end=" ")