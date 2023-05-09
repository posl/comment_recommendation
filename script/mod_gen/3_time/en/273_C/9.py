def count_greater_than(A, x):
    from bisect import bisect_right
    return len(A) - bisect_right(A, x)

if __name__ == '__main__':
    count_greater_than()