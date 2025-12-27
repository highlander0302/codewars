"""Generate fibanaci numbers with function."""


def generate_fibonaci(n: int) -> list[int]:
    if n < 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib_list = generate_fibonaci(n - 1)
    next_n = fib_list[-1] + fib_list[-2]
    fib_list.append(next_n)

    return fib_list


result = generate_fibonaci(10)
print(result)
