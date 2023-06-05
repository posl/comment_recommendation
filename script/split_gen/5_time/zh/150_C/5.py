def get_min_permutation(n):
    if n == 1:
        return [1]
    else:
        return [n] + get_min_permutation(n - 1)
