def comb(n,r):
    if n == 0 or r == 0:
        return 1
    if n < r:
        return 0
    return comb(n-1,r-1) + comb(n-1,r)

if __name__ == '__main__':
    comb()