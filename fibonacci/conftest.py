from datetime import datetime, timedelta
from typing import Callable
import pytest


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"total runtime: {diff.total_seconds()}")


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_validate_runtime(*args, **kw):
        tick = datetime.now()
        result = method(*args, **kw)
        tock = datetime.now()
        runtime = tock - tick
        print(f"total runtime: {runtime.total_seconds()}")

        if runtime > runtime_limit:
            raise RuntimeError(
                f"Runtime is too long: {runtime.total_seconds()}")

        return result

    return run_function_and_validate_runtime
