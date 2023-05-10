def get_permutation_count(n):
    if n <= 1:
        return 1
    else:
        return n * get_permutation_count(n - 1)
