# Uses python3
import sys
sys.path.append('../app')

from fibonacci_number.fibonacci_table import calc_fib
# from .last_digit_of_fibonacci_number.fibonacci_last_digit_table import get_fibonacci_last_digit_table
n = int(input())

# for i in range(990, 1001):
#     for N in range(n):
#         if i >= 2:
#             print(calc_fib(N) % i , end=" ")
#         else:
#             print(calc_fib(N), end=" ")
#     print('\n')

for i in range(n):
        print(calc_fib(i), end=" ")
# print('\n')

