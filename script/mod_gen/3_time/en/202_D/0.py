def nCr(n,r):
    r = min(r,n-r)
    numer = reduce(op.mul,xrange(n,n-r,-1),1)
    denom = reduce(op.mul,xrange(1,r+1),1)
    return numer//denom

if __name__ == '__main__':
    nCr()