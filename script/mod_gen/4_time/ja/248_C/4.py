def comb(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return comb(n-1, r-1) + comb(n-1, r)

if __name__ == '__main__':
    comb()