def fibonacci_naive(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)