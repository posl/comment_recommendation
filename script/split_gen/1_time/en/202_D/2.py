def nCr(n,r):
    if n<r:
        return 0
    else:
        r = min(r,n-r)
        numer = reduce(op.mul,xrange(n,n-r,-1),1)
        denom = reduce(op.mul,xrange(1,r+1),1)
        return numer//denom
import operator as op
A,B,K = map(int,raw_input().split())
