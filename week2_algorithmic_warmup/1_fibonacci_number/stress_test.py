from fibonacci_table import calc_fib as calc_fib_table
from fibonacci_naive import calc_fib as calc_fib_naive

# Uses python3
for i in range(31):
    fib_table = calc_fib_table(i)
    fib_naive = calc_fib_naive(i)
    if fib_table == fib_naive:
        print(i, fib_table)
    else:
        print("Wrong Answer: " + str(i), "Fib_table = " + str(fib_table), "Fib_naive = " + str(fib_naive))
        break
