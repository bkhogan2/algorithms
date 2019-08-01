# Uses python3
import sys
sys.path.append('../')

from fibonacci_number.fibonacci_table import calc_fib

def get_period_length(n,m):
    period = []
    
    i = 0
    while True:
        if i >= 2:
            period.append(calc_fib(i) % m)
        else:
            period.append(i)

        if i >=2 and period[i-1] == 0 and period[i] == 1:
            break

        i = i + 1

    return len(period) - 2

def get_fibonacci_huge_fast(n, m):
    length = get_period_length(n,m)
    return calc_fib(n % length) % m

n = int(input())
m = int(input())

print(get_fibonacci_huge_fast(n,m))