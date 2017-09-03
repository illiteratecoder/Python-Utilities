"""Decorator function to print runtime of a given function."""

def get_runtime(func):
    def f(*args, **kwargs):
        from time import time

        start = time()
        val = func(*args, **kwargs)
        end = time()
        print("--- Runtime: {} seconds ---".format(start - end))
        return val

    return f
