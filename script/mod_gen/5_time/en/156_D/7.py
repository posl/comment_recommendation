def comb(n, r):
    if n < r:
        return 0
    elif r == 0:
        return 1
    else:
        return comb(n-1, r-1) * n // r
n,a,b = map(int,input().split())
mod = 10**9 + 7
print((pow(2,n,mod)-1-comb(n,a)-comb(n,b))%mod)

if __name__ == '__main__':
    comb()