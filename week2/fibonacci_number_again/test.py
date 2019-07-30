# Uses python3
from .fibonacci_number.fibonacci_table import calc_fib
# from fibonacci_last_digit_table import get_fibonacci_last_digit_table

n = int(input())

# for N in get_fibonacci_last_digit_table(n):
#     print(N, end=" ")

for N in calc_fib(n):
    print(N, end=" ")