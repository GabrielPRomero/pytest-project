import pytest
from fibonacci.dynamic import better_fibonacci_dynamic, fibonacci_dynamic
from fibonacci.conftest import track_performance
from time import sleep

@pytest.mark.performance
@track_performance
def test_performance():
    # sleep(3) fails the test
    better_fibonacci_dynamic(1000)