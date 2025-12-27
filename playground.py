from functools import wraps
from typing import Any, Callable


def before_after_decorator(func: Callable[[str], None]) -> Callable[[str], None]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        print("before hello")
        func(*args, **kwargs)
        print("after hello")

    return wrapper


@before_after_decorator
def say_hallo(name: str) -> None:
    print(f"hey to {name}!")
