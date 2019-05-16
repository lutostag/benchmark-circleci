import time

def test_my_stuff(benchmark):
    benchmark(time.sleep, 0.10)


def fib(a):
    if a <= 0:
        return 0
    if a == 1:
        return 1
    return fib(a-1) + fib(a-2)

def test_fib(benchmark):
    benchmark(fib, 35)
