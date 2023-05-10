def get_permutation(n, k):
    if n == 1:
        return [1]
    elif n == 2:
        if k == 1:
            return [1, 2]
        else:
            return [2, 1]
    else:
        if k == 1:
            return [1] + get_permutation(n - 1, 1)
        elif k == 2:
            return [2] + get_permutation(n - 1, 1)
        elif k == 3:
            return [2] + get_permutation(n - 1, 2)
        else:
            return [k - 1] + get_permutation(n - 1, k - 2)
