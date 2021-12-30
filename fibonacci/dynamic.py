def fibonacci_dynamic(n: int) -> int:
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]

def better_fibonacci_dynamic(n: int) -> int:
    fib_1, fib_2 = 0, 1
    
    for i in range(1, n + 1):
        f1 = fib_1 + fib_2
        fib_1, fib_2 = fib_2, f1
    return fib_1