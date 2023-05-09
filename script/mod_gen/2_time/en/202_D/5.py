def nCr(n,r):
    if n<r:
        return 0
    elif n==r:
        return 1
    else:
        return nCr(n-1,r-1) + nCr(n-1,r)

if __name__ == '__main__':
    nCr()