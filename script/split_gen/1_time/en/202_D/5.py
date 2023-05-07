def nCr(n,r):
    return int( reduce(lambda x,y:x*y, range(n-r+1, n+1)) / reduce(lambda x,y:x*y, range(1, r+1)) )
