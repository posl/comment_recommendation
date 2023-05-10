def get_permutation(n):
    if n == 1:
        return [[1]]
    else:
        return [[n] + p for p in get_permutation(n-1)] + [p + [n] for p in get_permutation(n-1)]
