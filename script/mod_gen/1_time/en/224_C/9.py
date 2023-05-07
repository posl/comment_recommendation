def combination(n, r):
    if r == 0:
        return 1
    return combination(n-1, r-1) * n // r

if __name__ == '__main__':
    combination()