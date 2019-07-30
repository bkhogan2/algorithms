# Uses python3
def calc_fib(n):
    fib_table = []

    for i in range(n + 1):
        if i <= 1:
            fib_table.append(i)
        else:
            fib_table.append(fib_table[i-2] + fib_table[i-1])

    return fib_table[-1]

# n = int(input())
# print(calc_fib(n))