def is_permutation(n, a):
    if len(a) != n:
        return False
    for i in range(1, n+1):
        if i not in a:
            return False
    return True

if __name__ == '__main__':
    is_permutation()