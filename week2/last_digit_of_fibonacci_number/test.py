# Uses python3
from fibonacci_last_digit import get_fibonacci_last_digit_naive
from fibonacci_last_digit_table import get_fibonacci_last_digit_table

for i in range(51):
    if get_fibonacci_last_digit_naive(i) == get_fibonacci_last_digit_table(i):
        print(i, get_fibonacci_last_digit_table(i))
    else:
        print("Wrong answer: ", i, get_fibonacci_last_digit_naive(i), get_fibonacci_last_digit_table(i))