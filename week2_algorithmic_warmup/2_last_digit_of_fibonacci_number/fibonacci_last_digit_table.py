# Uses python3
import sys

def get_fibonacci_last_digit_table(n):
    fib_table = []

    for i in range(n+1):
        if i <= 1:
            fib_table.append(i)
        else:
            fib_table.append((fib_table[i-2] + fib_table[i-1])%10)
        
    return fib_table[-1]