def count_greater_than(A, x):
    from bisect import bisect_right
    return len(A) - bisect_right(A, x)
