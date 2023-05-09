def is_permutation(n, a):
    if n != len(a):
        return False
    a.sort()
    for i in range(1, n+1):
        if i != a[i-1]:
            return False
    return True

if __name__ == '__main__':
    is_permutation()