def is_permutation_of_n(n, a):
    if len(a) != n:
        return False
    for i in range(n):
        if i+1 not in a:
            return False
    return True
