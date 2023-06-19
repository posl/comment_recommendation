def comb(n,r):
    if r == 0:
        return 1
    else:
        return comb(n,r-1)*(n-r+1)//r
N,M = map(int,input().split())
print(comb(N,2) - M)
