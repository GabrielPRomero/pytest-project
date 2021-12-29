from fibonacci.naive import fibonacci_naive
from fibonacci.cached import fibo_memo
import pytest
from typing import List, Tuple, Callable, Dict

Decorator = Callable


# def my_parametrize(indentifiers: str, values: List[Tuple[int, int]]) -> Decorator:
#     def my_parametrize_decorator(function: Callable) -> Callable:
#         def run_function_parametrize() -> None:
#             list_of_kwargs = get_list_of_kwargs(indentifiers, values)

#             for kwargs_for_function in list_of_kwargs:
#                 function(**kwargs_for_function)
#     return my_parametrize_decorator


# @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)])
# # @my.parametrize(identifiers="n, expected", values=[(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)])
# def test_naive(n: int, expected: int) -> None:
#     res = fibonacci_naive(n)
#     assert res == expected


# @pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)])
# def test_mmeoized(n: int, expected: int) -> None:
#     res = fibo_memo(n)
#     assert res == expected

@pytest.mark.parametrize("fib_func", [fibonacci_naive, fibo_memo])
@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)])
def test_fibonacci(fib_func: Callable[[int], int], n: int, expected: int) -> None:
    res = fib_func(n)
    assert res == expected
