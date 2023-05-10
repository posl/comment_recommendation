def perm(n, r):
    if n < r:
        return 0
    else:
        return fact(n) // fact(n - r)

if __name__ == '__main__':
    perm()