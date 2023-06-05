def is_permutation(n, a):
    for i in range(1, n+1):
        if i not in a:
            return False
    return True
