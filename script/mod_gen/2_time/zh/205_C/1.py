def is_permutation(n, a):
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            return False
    return True

if __name__ == '__main__':
    is_permutation()