def func(n,a,b):
    mod = 10**9+7
    if a+b>n+1:
        return 0
    else:
        return pow(2,n,mod) - (comb(n,a,mod)+comb(n,b,mod))%mod
